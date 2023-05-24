const TelesignSDK = require('telesignenterprisesdk');

// Replace the defaults below with your Telesign authentication credentials or pull them from environment variables.
const customerId = process.env.CUSTOMER_ID || "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
const apiKey = process.env.API_KEY || "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

// Set the default below to your test phone number or pull it from an environment variable.
// In your production code, update the phone number dynamically for each purchase.
const phoneNumber = process.env.PHONE_NUMBER || "11234567890";

// Generate one-time passcode (OTP) and add it to request parameters.
const verifyCode = Math.floor(Math.random() * 99999).toString();
const params = {
    verify_code: verifyCode
};

// Instantiate a verification client object.
const client = new TelesignSDK(customerId, apiKey);

// Define the callback.
function smsVerifyCallback(error, responseBody) {
    if (error === null) {
        // Display the response body in the console for debugging purposes. 
        // In your production code, you would likely remove this.
        console.log("\nResponse body:\n" + JSON.stringify(responseBody));
    } else {
        console.error("Unable to send SMS. Error:\n\n" + error);
    }
    // Display prompt to enter asserted OTP in the console.
    // In your production code, you would instead collect the asserted OTP from the end-user.
    prompt('\nEnter the verification code you received:\n', verify);
}

function prompt(question, callback) {
    const stdin = process.stdin, stdout = process.stdout;
    stdin.resume();
    stdout.write(question);
    stdin.once('data', function (data) {
        callback(data.toString().trim());
    });
}

// Determine if the asserted OTP matches your original OTP, and resolve the login attempt accordingly. 
// You can simulate this by reporting whether the codes match.
function verify(input) {
    if (input === params['verify_code']) {
        console.log('\nYour code is correct.');
    } else {
        console.log('\nYour code is incorrect.');
    }
    process.exit();
}

// Make the request and capture the response.
client.verify.sms(smsVerifyCallback, phoneNumber, params);