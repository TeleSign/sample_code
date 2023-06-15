<?php
require __DIR__ . "/../vendor/autoload.php";
use telesign\enterprise\sdk\verify\VerifyClient;
use function telesign\sdk\util\randomWithNDigits;

# Replace the defaults below with your Telesign authentication credentials or pull them from environment variables.
# Replace the defaults below with your Telesign authentication credentials or pull them from environment variables.
$customer_id = getenv('CUSTOMER_ID') ?? 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890';
$api_key = getenv('API_KEY') ?? 'ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==';

# Set the default below to your test phone number or pull it from an environment variable. 
# In your production code, update the phone number dynamically for each transaction.
$phone_number = getenv('PHONE_NUMBER') ?? '11234567890';

# Generate one-time passcode (OTP) for verification.
$verify_code = randomWithNDigits(5);

# Instantiate a verification client object.
$verify_client = new VerifyClient($customer_id, $api_key);

# Make the request and capture the response.
$response = $verify_client->sms($phone_number, [ "verify_code" => $verify_code ]);

# Display the response in the console for debugging purposes. 
# In your production code, you would likely remove this.
echo("\nResponse HTTP status:\n");
print_r($response->status_code);
echo("\nResponse body: \n");
print_r($response->json);

# Display prompt to enter asserted OTP in the console.
# In your production code, you would instead collect the asserted OTP from the end-user.
echo "Please enter the verification code you were sent: ";
$user_entered_verify_code = rtrim(fgets(STDIN));

# Determine if the asserted OTP matches your original OTP, and resolve the login attempt accordingly. 
# You can simulate this by reporting whether the codes match.
if ($user_entered_verify_code == $verify_code) {
    echo "Your code is correct.\n";
} else {
    echo "Your code is incorrect.\n";
}

?>