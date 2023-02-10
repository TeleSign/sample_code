import java.io.IOException;
import java.util.Base64;

import org.asynchttpclient.AsyncHttpClient;
import org.asynchttpclient.DefaultAsyncHttpClient;

public class App {
    public static void main(String[] args) throws IOException {
		String customerId = System.getenv().getOrDefault("CUSTOMER_ID", "ABC1DE23-A12B-1234-56AB-AB1234567890");
        String apiKey = System.getenv().getOrDefault("API_KEY", "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==");

        String phoneNumber = System.getenv().getOrDefault("PHONE_NUMBER", "1234567890");

		AsyncHttpClient client = new DefaultAsyncHttpClient();
		client.prepare("POST", "https://rest-ww.telesign.com/v1/verify/sms")
		  .setHeader("accept", "application/json")
		  .setHeader("content-type", "application/x-www-form-urlencoded")
		  .setHeader("authorization", createBasicAuthString(phoneNumber, apiKey))
		  .setBody(String.format("is_primary=true&phone_number=%s", phoneNumber))
		  .execute()
		  .toCompletableFuture()
		  .thenAccept(System.out::println)
		  .join();

		client.close();
	}
    
    public static String createBasicAuthString(String customer_id, String api_key){
    	String auth_string ="";
    	auth_string = customer_id +":" + api_key;
    	auth_string = Base64.getEncoder().encodeToString(auth_string.getBytes());
    	auth_string = "Basic " + auth_string;
    	
    	return auth_string;
    }
}
