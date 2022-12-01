const TelesignSDK = require('telesignenterprisesdk');

// Replace the defaults below with your Telesign authentication credentials.
const customerId = process.env.CUSTOMER_ID || "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
const apiKey = process.env.API_KEY || "TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

// Set the default below to your test phone number. In your production code, update the phone number dynamically for each purchase.
const phoneNumber = process.env.PHONE_NUMBER || "15558675309";

// Generate verification code and add it to request parameters.
const verifyCode = Math.floor(Math.random() * 99999).toString();
const params = {
    verify_code: verifyCode
};

// Make the request and capture the response.
const client = new TelesignSDK(customerId, apiKey);
client.verify.sms(smsVerifyCallback, phoneNumber, params);

function smsVerifyCallback(error, responseBody) {
    if (error === null) {
        // Display the response body in the console for debugging purposes. In your production code, you would likely remove this.
        console.log(`\nMessaging response for messaging phone number: ${phoneNumber}\n` +
            `  code: ${responseBody['status']['code']}\n` +
            `  description: ${responseBody['status']['description']}`);
    } else {
        console.error("Unable to send SMS. Error:\n\n" + error);
    }
    // Display prompt to enter verification code in the console.
    // In your production code, you would instead collect the potential verification code from the end-user in your platform's interface.
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

function verify(input) {
    if (input === params['verify_code']) {
        console.log('\nYour code is correct.');
    } else {
        console.log('\nYour code is incorrect.');
    }
    process.exit();
}