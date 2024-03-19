package phoneidcontact;

import java.util.Dictionary;
import java.util.HashMap;
import com.telesign.RestClient;
import com.telesign.PhoneIdClient; 

public class App {
    public static void main(String[] args) {

        // Replace the defaults below with your Telesign authentication credentials or pull them from environment variables.
        String customerId = System.getenv().getOrDefault("CUSTOMER_ID", "FFFFFFFF-EEEE-DDDD-1234-AB1234567890");
        String apiKey = System.getenv().getOrDefault("API_KEY", "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==");

        // Set the default below to your test phone number or pull it from an environment variable. 
        // In your production code, update the phone number dynamically for each transaction.
        String phoneNumber = System.getenv().getOrDefault("PHONE_NUMBER", "11234567890");

        // Create an object to hold other parameter values.
        HashMap<String, Object> contact = new HashMap<>();
        contact.put("contact", new HashMap<>());
        HashMap<String, Object> otherParams = new HashMap<>();
        otherParams.put("addons", contact);

        try {
            // Instantiate a Phone ID client object.
            PhoneIdClient pidClient = new PhoneIdClient(customerId, apiKey);

            // Make the request and capture the response.
            RestClient.TelesignResponse telesignResponse = pidClient.phoneid(phoneNumber, otherParams);
            
            // Display the response body in the console for debugging purposes. 
            // In your production code, you would likely remove this.
            System.out.println(telesignResponse.statusCode);
            System.out.println(telesignResponse.body);
        } catch (Exception e) {
            System.out.println((char)27 + "[31m" + "\nAn exception occurred.\nERROR: " + e.getMessage());
        }
    }
}
