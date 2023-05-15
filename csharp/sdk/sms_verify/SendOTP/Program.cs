using System;
using System.Collections.Generic;
using Telesign;
using TelesignEnterprise;

namespace SendOTP
{
    class SendOTP
    {
        public static void Main(string[] args)
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

            // Generate one-time passcode (OTP) and add it to request parameters.
            Random random = new Random();
            int num = random.Next(100000);
            string verifyCode = num.ToString();
            Dictionary<string, string> parameters = new Dictionary<string, string>();
            parameters.Add("verify_code", verifyCode);

            try
            {
                // Instantiate a verification client object.
                VerifyClient verifyClient = new VerifyClient(customerId, apiKey);

                // Make the request and capture the response.
                RestClient.TelesignResponse telesignResponse = verifyClient.Sms(phoneNumber, parameters);

                // Display the response in the console for debugging purposes. 
                // In your production code, you would likely remove this.
                Console.WriteLine(string.Format("\nResponse HTTP status:\n{0}",telesignResponse.StatusCode));
                Console.WriteLine(string.Format("Response body:\n{0}\n",telesignResponse.Body));

                // Display prompt to enter asserted OTP in the console.
                // In your production code, you would instead collect the asserted OTP from the end-user.
                Console.WriteLine("Please enter your verification code:");
                string code = Console.ReadLine().Trim();

                // Determine if the asserted OTP matches your original OTP, and resolve the login attempt accordingly. 
                // You can simulate this by reporting whether the codes match.
                if (verifyCode == code)
                {
                    Console.WriteLine("Your code is correct.");
                }
                else
                {
                    Console.WriteLine("Your code is incorrect.");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("ERROR: An exception occured.");
            }
        }
    }
}