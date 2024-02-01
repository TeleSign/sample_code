using System;
using System.Text.Json.Nodes;
using Telesign;
using Newtonsoft.Json;
using System.Runtime.InteropServices;

namespace SendPNtoPIDContact
{
    class SendPNtoPIDContact
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

            try
            {
                // Instantiate a Phone ID client object.
                PhoneIdClient phoneIdClient = new PhoneIdClient(customerId, apiKey);

                // Add the payload
                object contact = new object(){};
                Dictionary<string, object> payload = new Dictionary<string, object>();
                payload.Add("addons", contact);

                // Make the request and capture the response.
                RestClient.TelesignResponse telesignResponse = phoneIdClient.PhoneId(phoneNumber, payload);

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
