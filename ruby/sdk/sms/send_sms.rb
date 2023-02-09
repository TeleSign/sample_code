require 'telesign'

# Replace the defaults below with your Telesign authentication credentials.
customer_id = ENV['CUSTOMER_ID'] || 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890'
api_key = ENV['API_KEY'] || 'ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=='

# Set the request inputs.
# Set the default below to your test phone number. In your production code, update the phone number dynamically for each transaction.
phone_number = ENV['PHONE_NUMBER'] || '15551212'
message = 'Hello world'
message_type = 'ARN'

# Make the request and capture the response.
client = Telesign::MessagingClient.new(customer_id, api_key)
response = client.message(phone_number, message, message_type)