from telesignenterprise.verify import VerifyClient
import os

# Replace the defaults below with your Telesign authentication credentials.
customer_id = os.getenv('CUSTOMER_ID', 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890')
api_key = os.getenv('API_KEY', 'ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==')

# Set the default below to your test phone number. 
# In your production code, update the phone number dynamically for each transaction.
phone_number = os.getenv('PHONE_NUMBER', '11234567890')


# Instantiate a verification client object.
verify = VerifyClient(customer_id, api_key)

# Make the request and capture the response.
response = verify.sms(phone_number)

# Display the response in the console for debugging purposes. 
# In your production code, you would likely remove this.
print(f"\nResponse HTTP status:\n{response.status_code}\n")
print(f"\nResponse body:\n{response.body}\n")

# Display prompt to enter asserted OTP in the console.
# In your production code, you would instead collect the asserted OTP from the end-user.
user_entered_verify_code = input("Please enter the verification code you were sent: ")

# Check if Telesign reports that the asserted OTP matches your original OTP, and resolve the login attempt accordingly.
# You can simulate this by reporting whether the codes match.
status = verify.status(response.json['reference_id'], verify_code=user_entered_verify_code).json['verify']['code_state']
if status == 'VALID':
    print("Your code is correct.")
else:
    print("Your code is incorrect.")