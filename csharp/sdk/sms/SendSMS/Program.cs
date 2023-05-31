using System;
using Telesign;

namespace SendSMS
{
    class SendSMS
    {
        static void Main(string[] args)
        {
            // Replace the defaults below with your Telesign authentication credentials.
            string customerId = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
            string apiKey = "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";
            
            // Set the default below to your test phone number. 
            // In your production code, update the phone number dynamically for each transaction.    
            string phoneNumber = "11234567890";

            // (Optional) Pull values from environment variables instead of hardcoding them.
            if (System.Environment.GetEnvironmentVariable("CUSTOMER_ID") != null) {
                customerId = System.Environment.GetEnvironmentVariable("CUSTOMER_ID");
            }
            
            if (System.Environment.GetEnvironmentVariable("API_KEY") != null) {
                apiKey = System.Environment.GetEnvironmentVariable("API_KEY");
            }

            if (System.Environment.GetEnvironmentVariable("PHONE_NUMBER") != null) {
                phoneNumber = System.Environment.GetEnvironmentVariable("PHONE_NUMBER");
            }

            // Set the message text and type.
            string message = "Your package has shipped! Follow your delivery at https://vero-finto.com/orders/3456";
            string messageType = "ARN";

            try
            {
                // Instantiate a messaging client object.
                MessagingClient messagingClient = new MessagingClient(customerId, apiKey);

                // Make the request and capture the response.
                RestClient.TelesignResponse telesignResponse = messagingClient.Message(phoneNumber, message, messageType);

                // Display the response in the console for debugging purposes. 
                // In your production code, you would likely remove this.
                Console.WriteLine("\nResponse HTTP status:\n" + telesignResponse.StatusCode);
                Console.WriteLine("\nResponse body:\n" + telesignResponse.Body);

            }
            catch (Exception e)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("\nAn exception occured.\nERROR: " + e.Message + "\n");
                Console.ResetColor();
            }

            Console.WriteLine("Press any key to quit.");
            Console.ReadKey();

            return;

        }
    }
}
