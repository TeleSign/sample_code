from requests import Request, Session, get
import os
from random import SystemRandom
import sys
sys.path.append('../../shared/')
import ts_auth


def prep_request(request):
    request_prepped = request.prepare()
    request_properties = {
        "method": request_prepped.method,
        "headers": request_prepped.headers,
        "body": request_prepped.body,
        "url": request_prepped.url
    }
    if auth_method == "basic":
        request_prepped.headers = ts_auth.add_basic(request_properties, customer_id, api_key)
    elif auth_method == "digest":
        request_prepped.headers = ts_auth.add_digest(request_properties, customer_id, api_key)
    else:
        print("Valid auth method not specified.")

    return request_prepped


# Specify which auth method to use, "basic" or "digest"
auth_method = "digest"

# Replace the defaults below with your Telesign authentication credentials
customer_id = os.getenv('CUSTOMER_ID', 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890')
api_key = os.getenv('API_KEY', 'ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==')

# Set the REST API URL
base_url = "https://rest-ww.telesign.com/v1/verify/"
verify_url = base_url + "sms"

# Set the request inputs.
# Set the default below to your test phone number. In your production code, update the phone number dynamically for each transaction.
phone_number = os.getenv('PHONE_NUMBER', '+447975777666')

# Set PSD2 dynamic linking. In your production code, update these values dynamically for each purchase.
transaction_payee = "Viatu"
transaction_amount = "40 pounds"

# Specify the language. This triggers the service to use the relevant pre-written PSD2/SCA templates. By default the service uses the American English template.
lang = "en-GB"

# Add all headers except auth headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Date': ts_auth.format_current_date()
}

# Create the payload
payload = f"phone_number={phone_number}&transaction_payee={transaction_payee}&transaction_amount={transaction_amount}&language={lang}"

# Create session and prepped request
s = Session()
req = Request('POST', verify_url, data=payload, headers=headers)
prepped_request = prep_request(req)

# Make the request and capture the response.
response = s.send(prepped_request)

# Display the request and response in the console for debugging purposes. In your production code, you would likely remove this.
ts_auth.pretty_print_request(prepped_request)
print(f"Response:\n{response.text}\n")

# Display prompt to enter verification code in the console.
# In your production code, you would instead collect the potential verification code from the end-user in your platform's interface.
user_entered_verify_code = input("Please enter the verification code you were sent: ")
status_url = base_url + response.json()['reference_id'] + "?verify_code=" + user_entered_verify_code
headers2 = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Date': ts_auth.format_current_date()
}
# Get status of the transaction from Telesign
s2 = Session()
req2 = Request('GET', status_url, headers=headers2)
prepped_request2 = prep_request(req2)
response2 = s.send(prepped_request2)
status = response2.json()['verify']['code_state']
if status == 'VALID':
    print("Your code is correct.")
else:
    print("Your code is incorrect.")
