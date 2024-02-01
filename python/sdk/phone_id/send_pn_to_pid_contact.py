import os

from telesign.phoneid import PhoneIdClient


# Replace the defaults below with your Telesign authentication credentials or pull them from environment variables.
customer_id = os.getenv('CUSTOMER_ID', 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890')
api_key = os.getenv('API_KEY', 'ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==')

# Set the default below to your test phone number or pull it from an environment variable. 
# In your production code, update the phone number dynamically for each transaction.
#phone_number = os.getenv('PHONE_NUMBER', '11234567890')
phone_number = '16262026728'

# Instantiate a Phone ID client object.
pid = PhoneIdClient(customer_id, api_key,  rest_endpoint='https://phoneid-api-ci.c11.telesign.com')

# Add the payload

print("\nPhone number:{}\n".format(phone_number))

payload = {  
    "addons": {
        "contact": {}
    },
    "phone_number": phone_number,
    "tst-phoneid-fake": True
}

# Make the request and capture the response. 
response = pid.phoneid(payload)

# Display the response body in the console for debugging purposes. 
# In your production code, you would likely remove this.
print(f"\nResponse:\n{response.body}\n")