<?php
require __DIR__ . "/../vendor/autoload.php";
use telesign\sdk\score\ScoreClient;

# Replace the defaults below with your Telesign authentication credentials or pull them from environment variables.
$customer_id = getenv('CUSTOMER_ID') ?? 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890';
$api_key = getenv('API_KEY') ?? 'ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==';
# Set the default below to your test phone number or pull it from an environment variable. 
# In your production code, update the phone number dynamically for each transaction.
$phone_number = getenv('PHONE_NUMBER') ?? '11234567890';

# Set a parameter for the account lifecycle stage the end user is in.
$account_lifecycle_event = "create";

# Instantiate an Intelligence client object.
$intelligence = new ScoreClient($customer_id, $api_key);

# Make the request and capture the response.
# The request_risk_insights flag is needed to use the latest version of Intelligence.
$response = $intelligence->score($phone_number, $account_lifecycle_event, ["request_risk_insights" => "true"]);

# Display the response body in the console for debugging purposes. 
# In your production code, you would likely remove this.
print_r($response->json);
?>
