const TelesignSDK = require('telesignenterprisesdk');

const customerId = process.env.CUSTOMER_ID || "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
const apiKey = process.env.API_KEY || "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

const phoneNumber = process.env.PHONE_NUMBER || "11234567890";

const verifyCode = Math.floor(Math.random() * 99999).toString();
const params = {
    verify_code: verifyCode
};

const client = new TelesignSDK(customerId, apiKey);
client.verify.sms(smsVerifyCallback, phoneNumber, params);

function smsVerifyCallback(error, responseBody) {
    if (error === null) {
        console.log("\nResponse:\n" + JSON.stringify(responseBody));
    } else {
        console.error("Unable to send message. " + error);
    }
    prompt('\nPlease enter the verification code you were sent:\n', verify);
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