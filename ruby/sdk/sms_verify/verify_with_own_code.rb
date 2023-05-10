require 'telesign'
require 'telesignenterprise'

# Replace the defaults below with your Telesign authentication credentials.
customer_id = ENV['CUSTOMER_ID'] || 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890'
api_key = ENV['API_KEY'] || 'ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=='

# Set the request inputs.
# Set the default below to your test phone number. In your production code, update the phone number dynamically for each transaction.
phone_number = ENV['PHONE_NUMBER'] || '11234567890'
verify_code = Telesign::Util.random_with_n_digits(5)

# Make the request and capture the response.
verify_client = TelesignEnterprise::VerifyClient.new(customer_id, api_key)
response = verify_client.sms(phone_number, verify_code: verify_code)

# Display the response in the console for debugging purposes. In your production code, you would likely remove this.
print "\nResponse HTTP status: ", response.status_code, "\n"
print "Response body: ", response.body, "\n\n"

# Display prompt to enter verification code in the console.
# In your production code, you would instead collect the potential verification code from the end-user in your platform's interface.
print 'Please enter the verification code you were sent: '
user_entered_verify_code = gets.strip

if verify_code == user_entered_verify_code
  puts 'Your code is correct.'
else
  puts 'Your code is incorrect.'
end