var TeleSignSDK = require('telesignsdk');

const customerId = process.env.CUSTOMER_ID || "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
const apiKey = process.env.API_KEY || "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

const phoneNumber = process.env.PHONE_NUMBER || "1234567890";

const message = "Hello world";
const messageType = "ARN";

const client = new TeleSignSDK( customerId, apiKey);

function printResponse(error, responseBody) {
    if (error === null) {
        console.log("## Response: ##");
        console.log(responseBody);
    } else {
        console.error("Unable to send message. " + error);
    }
}

client.sms.message(printResponse, phoneNumber, message, messageType);



