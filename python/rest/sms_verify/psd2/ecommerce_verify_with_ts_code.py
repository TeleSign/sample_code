import requests
import base64
import os


# Format HTTP request to print for debugging purposes.
def format_prepped_request(prepped, encoding=None):
    encoding = encoding or requests.utils.get_encoding_from_headers(prepped.headers)
    body = prepped.body.decode(encoding) if encoding else '<binary data>'
    headers = '\n'.join(['{}: {}'.format(*hv) for hv in prepped.headers.items()])
    return f"""\
{prepped.method} {prepped.path_url}
{headers}
{body}"""


# Replace the defaults below with your TeleSign authentication credentials from https://teleportal.telesign.com
customer_id = os.getenv('CUSTOMER_ID', 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890')
api_key = os.getenv('API_KEY', 'TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==')

# Set the REST API URLs
base_url = "https://rest-ww.telesign.com/v1/verify/"
verify_url = base_url + "sms"

# Set the SMS Verify inputs. In your production code, update the phone number dynamically for each purchase.
# Set the default below to your test phone number. In your production code, update the phone number dynamically for each purchase.
phone_number = os.getenv('PHONE_NUMBER', '+447975777666')

# Set PSD2 dynamic linking. In your production code, update these values dynamically for each purchase.
transaction_payee = "Viatu"
transaction_amount = "€95"

# Specify the language. This triggers the service to use one of our pre-written PSD2/SCA templates.
lang = "en-GB"

# Generate auth string and add it to the request headers
auth_string = customer_id + ":" + api_key
auth_string = base64.b64encode(auth_string.encode())
auth_string = auth_string.decode("utf-8")
auth_string = "Basic " + auth_string
headers = {
	"Authorization": auth_string,
	"Content-Type":"application/x-www-form-urlencoded"
}

# Create the payload
payload = f"phone_number={phone_number}&transaction_payee={transaction_payee}&transaction_amount={transaction_amount}&language={lang}"

# Make the request and capture the response.
# If SIM Swap indicates likelihood of real fraud, verification code is not sent.
# If Score indicates likelihood of friendly fraud, verification code is not sent.
response = requests.post(verify_url, headers=headers, data=payload.encode('utf-8'))
prepped_request = format_prepped_request(response.request, 'utf8')

# Display the request and response in the console for debugging purposes. In your production code, you would likely remove this.
print(f"\nVerify Request:\n{prepped_request}\n\nVerify Response:\n{response.text}\n")

# Display prompt to enter verification code in the console.
# In your production code, you would instead collect the potential verification code from the end-user in your platform's interface.
user_entered_verify_code = input("Please enter the verification code you were sent: ")
status_url = base_url + response.json()['reference_id'] + "?verify_code=" + user_entered_verify_code
response2 = requests.get(status_url, headers=headers)
status = response2.json()['verify']['code_state']
if status == 'VALID':
    print("Your code is correct.")
else:
    print("Your code is incorrect.")
