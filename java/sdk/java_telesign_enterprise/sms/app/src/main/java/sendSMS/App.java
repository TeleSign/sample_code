package sendSMS;

import com.telesign.RestClient;
import com.telesign.enterprise.MessagingClient;

public class App {
    public static void main(String[] args) {

        // Replace the defaults below with your Telesign authentication credentials or pull them from environment variables.
        String customerId = System.getenv().getOrDefault("CUSTOMER_ID", "FFFFFFFF-EEEE-DDDD-1234-AB1234567890");
        String apiKey = System.getenv().getOrDefault("API_KEY", "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==");

        // Set the default below to your test phone number or pull it from an environment variable.
        // In your production code, update the phone number dynamically for each purchase.
        String phoneNumber = System.getenv().getOrDefault("PHONE_NUMBER", "11234567890");

        // Set the message text and type.
        String message = "Your package has shipped! Follow your delivery at https://vero-finto.com/orders/3456";
        String messageType = "ARN";

        try {

            // Instantiate a messaging client object.
            MessagingClient messagingClient = new MessagingClient(customerId, apiKey);

            // Make the request and capture the response.
            RestClient.TelesignResponse telesignResponse = 	messagingClient.message(phoneNumber, message, messageType, null);

            // Display the response body in the console for debugging purposes. 
            // In your production code, you would likely remove this.
            System.out.println(telesignResponse.statusCode);
            System.out.println(telesignResponse.body);

        } catch (Exception e) {
            System.out.println((char)27 + "[31m" + "\nAn exception occurred.\nERROR: " + e.getMessage());
        }
    }
}
