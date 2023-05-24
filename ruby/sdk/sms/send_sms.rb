require 'telesign'

# Replace the defaults below with your Telesign authentication credentials or pull them from environment variables.
customer_id = ENV['CUSTOMER_ID'] || 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890'
api_key = ENV['API_KEY'] || 'ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=='

# Set the default below to your test phone number or pull it from an environment variable. 
# In your production code, update the phone number dynamically for each transaction.
phone_number = ENV['PHONE_NUMBER'] || '11234567890'

# Set the message text and type.
message = 'Your package has shipped!'
messageType = 'ARN'

# Instantiate a messaging client object.
client = Telesign::MessagingClient.new(customer_id, api_key)

# Make the request and capture the response.
response = client.message(phone_number, message, message_type)

# Display the response in the console for debugging purposes. 
# In your production code, you would likely remove this.
print "\nResponse HTTP status: ", response.status_code, "\n"
print "Response body: ", response.body, "\n\n"