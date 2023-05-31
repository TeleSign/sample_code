var TeleSignSDK = require('telesignsdk');

// Replace the defaults below with your Telesign authentication credentials or pull them from environment variables.
const customerId = process.env.CUSTOMER_ID || "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
const apiKey = process.env.API_KEY || "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

// Set the default below to your test phone number or pull it from an environment variable. 
// In your production code, update the phone number dynamically for each transaction.
const phoneNumber = process.env.PHONE_NUMBER || "11234567890";

// Set the message text and type.
const message = "Your package has shipped! Follow your delivery at https://vero-finto.com/orders/3456";
const messageType = "ARN";

// Instantiate a messaging client object.
const client = new TeleSignSDK( customerId, apiKey);

// Define the callback.
function smsCallback(error, responseBody) {
    // Display the response body in the console for debugging purposes. 
    // In your production code, you would likely remove this.
    if (error === null) {
        console.log("\nResponse body:\n" + JSON.stringify(responseBody));
    } else {
        console.error("Unable to send SMS. Error:\n\n" + error);
    }
}

// Make the request and capture the response.
client.sms.message(smsCallback, phoneNumber, message, messageType);



