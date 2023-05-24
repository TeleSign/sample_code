<?php
require __DIR__ . "/../vendor/autoload.php";
use telesign\sdk\messaging\MessagingClient;

# Replace the defaults below with your Telesign authentication credentials.
$customer_id = getenv('CUSTOMER_ID') ? getenv('CUSTOMER_ID') :'FFFFFFFF-EEEE-DDDD-1234-AB1234567890';
$api_key = getenv('API_KEY') ? getenv('API_KEY') :'ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==';

# Set the default below to your test phone number. 
# In your production code, update the phone number dynamically for each transaction.
$phone_number = getenv('PHONE_NUMBER') ? getenv('PHONE_NUMBER'):'11234567890';

# Set the message text and type.
$message = "Your package has shipped!";
$message_type = "ARN";

# Instantiate a messaging client object.
$messaging = new MessagingClient($customer_id, $api_key);

# Make the request and capture the response.
$response = $messaging->message($phone_number, $message, $message_type);

# Display the response body in the console for debugging purposes. 
# In your production code, you would likely remove this.
print_r($response->json);
?>