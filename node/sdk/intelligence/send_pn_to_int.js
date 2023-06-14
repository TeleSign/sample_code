var TeleSignSDK = require('telesignsdk');

// Replace the defaults below with your Telesign authentication credentials or pull them from environment variables.
const customerId = process.env.CUSTOMER_ID || "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
const apiKey = process.env.API_KEY || "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

// Set the default below to your test phone number or pull it from an environment variable. 
// In your production code, update the phone number dynamically for each transaction.
const phoneNumber = process.env.PHONE_NUMBER || "11234567890";

// Set a parameter for the account lifecycle stage the end user is in.
const account_lifecycle_event = "create";

// Set a flag to use the latest version of Intelligence.
const request_risk_insights="true"

// Instantiate a Telesign client object.
const client = new TeleSignSDK( customerId, apiKey);

// Define the callback.
function intCallback(error, responseBody) {
    // Display the response body in the console for debugging purposes. 
    // In your production code, you would likely remove this.
    if (error === null) {
        console.log("\nResponse body:\n" + JSON.stringify(responseBody));
    } else {
        console.error("An exception occurred. Error:\n\n" + error);
    }
}

// Make the request and capture the response. 
client.score.score(function (error, responseBody) {console.log("\nResponse body:\n" + JSON.stringify(responseBody))}, phoneNumber, account_lifecycle_event, null, null, null, null, request_risk_insights);
