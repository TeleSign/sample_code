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

            Random random = new Random();
            int num = random.Next(100000);
            string verifyCode = num.ToString();

            Dictionary<string, string> parameters = new Dictionary<string, string>();
            parameters.Add("verify_code", verifyCode);

            try
            {
                VerifyClient verifyClient = new VerifyClient(customerId, apiKey);
                RestClient.TelesignResponse telesignResponse = verifyClient.Sms(phoneNumber, parameters);

                Console.WriteLine("Please enter your verification code:");
                string code = Console.ReadLine().Trim();

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
                Console.WriteLine(e);
            }
        }
    }
}