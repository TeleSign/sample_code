package com.example.cellular
 
import android.content.Context
import android.net.ConnectivityManager
import android.net.Network
import android.net.NetworkCapabilities
import android.net.NetworkRequest
import androidx.annotation.NonNull
import io.flutter.embedding.engine.plugins.FlutterPlugin
import io.flutter.plugin.common.MethodCall
import io.flutter.plugin.common.MethodChannel
import io.flutter.plugin.common.MethodChannel.MethodCallHandler
import io.flutter.plugin.common.MethodChannel.Result
import java.io.IOException
import kotlinx.coroutines.*
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import okhttp3.Response
 
/** CellularPlugin */
class CellularPlugin : FlutterPlugin, MethodCallHandler {
    /// The MethodChannel that will the communication between Flutter and native Android
    /// This local reference serves to register the plugin with the Flutter Engine and unregister it
    /// when the Flutter Engine is detached from the Activity
 
    private lateinit var channel: MethodChannel
    private lateinit var context: Context
    private val _mainScope = CoroutineScope(Dispatchers.Main)
    val requestbuilder: NetworkRequest =
        NetworkRequest.Builder()
            .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
            .addTransportType(NetworkCapabilities.TRANSPORT_CELLULAR)
            .build()
    val builder: OkHttpClient.Builder = OkHttpClient.Builder()
 
    override fun onAttachedToEngine(
        @NonNull flutterPluginBinding: FlutterPlugin.FlutterPluginBinding
    ) {
        channel = MethodChannel(flutterPluginBinding.binaryMessenger, "cellular")
        context = flutterPluginBinding.applicationContext
 
        val connectivityManager =
            context.getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
 
        val networkCallback =
            object : ConnectivityManager.NetworkCallback() {
                override fun onUnavailable() {
                    super.onUnavailable()
                }
 
                override fun onLosing(network: Network, maxMsToLive: Int) {
                    super.onLosing(network, maxMsToLive)
                }
 
                override fun onAvailable(network: Network) {
                    val result = connectivityManager.bindProcessToNetwork(network)
                    super.onAvailable(network)
                }
 
                override fun onLost(network: Network) {
                    super.onLost(network)
                }
            }
 
        connectivityManager.requestNetwork(requestbuilder, networkCallback)
        channel.setMethodCallHandler(this)
    }
 
    override fun onMethodCall(@NonNull call: MethodCall, @NonNull result: Result) {
        _mainScope.launch {
            when (call.method) {
                "sendRequest" -> {
                    val url = call.argument<String>("url")
                    val method = call.argument<String?>("method")
                    val payload = call.argument<String?>("payload")
 
                    var response = ""
                    withContext(Dispatchers.IO) {
                        if (url != null) {
                            response = sendRequest(url, method as String, payload as String)
                        }
                    }
 
                    result.success(response)
                }
                else -> result.notImplemented()
            }
        }
    }
 
    override fun onDetachedFromEngine(@NonNull binding: FlutterPlugin.FlutterPluginBinding) {
        channel.setMethodCallHandler(null)
    }
 
    fun sendRequest(@NonNull url: String, method: String, payload: String): String {
 
        val connectivityManager =
            context.getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
 
        try {
            val client: OkHttpClient = builder.build()
            val request = Request.Builder().url(url)
 
            if (method == "POST") {
                val body = payload.toRequestBody("application/json".toMediaTypeOrNull())
                request.post(body)
            }
 
            val req = request.build()
            val response: Response = client.newCall(req).execute()
 
            return response.body!!.string()
        } catch (e: IOException) {
            return (e.toString())
        }
    }
}