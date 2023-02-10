using System;
using Telesign;

namespace SendSMS
{
    class SendSMS
    {
        static void Main(string[] args)
        {
            string customerId = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
            string apiKey = "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";
            string phoneNumber = "15558675309";

            if (System.Environment.GetEnvironmentVariable("CUSTOMER_ID") != null) {
                customerId = System.Environment.GetEnvironmentVariable("CUSTOMER_ID");
            }
            
            if (System.Environment.GetEnvironmentVariable("API_KEY") != null) {
                apiKey = System.Environment.GetEnvironmentVariable("API_KEY");
            }

            if (System.Environment.GetEnvironmentVariable("PHONE_NUMBER") != null) {
                phoneNumber = System.Environment.GetEnvironmentVariable("PHONE_NUMBER");
            }

            string message = "Hello world!";
            string messageType = "ARN";

            try
            {
                MessagingClient messagingClient = new MessagingClient(customerId, apiKey);
                RestClient.TelesignResponse telesignResponse = messagingClient.Message(phoneNumber, message, messageType);
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }

            Console.WriteLine("Press any key to quit.");
            Console.ReadKey();

            return;

        }
    }
}
