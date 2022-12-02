<?php
require __DIR__ . "/../vendor/autoload.php";
use telesign\enterprise\sdk\verify\VerifyClient;

# Replace the defaults below with your Telesign authentication credentials.
$customer_id = getenv('CUSTOMER_ID') ? getenv('CUSTOMER_ID') :'FFFFFFFF-EEEE-DDDD-1234-AB1234567890';
$api_key = getenv('API_KEY') ? getenv('API_KEY') :'TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==';

# Set the request inputs.
# Set the default below to your test phone number. In your production code, update the phone number dynamically for each transaction.
$phone_number = getenv('PHONE_NUMBER') ? getenv('PHONE_NUMBER'):'15551212';
$message = "Hello world from Telesign Enterprise SDK";
$message_type = "ARN";

# Make the request and capture the response.
$verify_client = new VerifyClient($customer_id, $api_key);
$response = $verify_client->sms($phone_number);

# Display the response body in the console for debugging purposes. In your production code, you would likely remove this.
print_r($response->json);
?>