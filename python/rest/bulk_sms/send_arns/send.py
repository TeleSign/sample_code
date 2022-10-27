from requests import Request, Session
import os
import sys

sys.path.append('../../shared/')
import ts_auth


# Replace the defaults below with your Telesign authentication credentials from https://teleportal.telesign.com
customer_id = os.getenv('CUSTOMER_ID', 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890')
api_key = os.getenv('API_KEY', 'TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==')

# Set the REST API URL
url = "https://rest-ww.telesign.com/v1/verify/bulk_sms"

# Set the SMS API inputs. In your production code, update the phone number dynamically for each purchase.
# Set the default below to your test phone number. In your production code, update the phone number dynamically for each purchase.
recipient_phone_numbers = [os.getenv('PHONE_NUMBER', '15551212')]
recipient_ids = ['bar']
phone_number_id_pairs = []

# Put your message text here
template = 'Hello World'

# Generate recipients string
for i in recipient_phone_numbers:
	phone_number_id_pairs[i] = recipient_phone_numbers[i] + ':' + recipient_ids[i]
recipients_string = ','.join(phone_number_id_pairs)

# Set ID for the entire transaction
external_id = 'foo'

# Add all headers except auth headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Date': ts_auth.format_current_date()
}

# Create the payload
payload = 'recipients={recipients}&template={template}&session_id={session_id}'.format(recipients=recipients_string, template=template, session_id=external_id)

# Create session and prepped request
s = Session()
req = Request('POST', url, data=payload, headers=headers)
prepped_request = req.prepare()

# Add auth to prepped request
request_properties = {
    "method": prepped_request.method,
    "headers": prepped_request.headers,
    "body": prepped_request.body,
    "url": prepped_request.url
}

prepped_request.headers = ts_auth.add_basic(request_properties, customer_id, api_key)
# prepped_request.headers = ts_auth.add_digest(request_properties, customer_id, api_key)

# Make the request and capture the response.
response = s.send(prepped_request)

# Display the request and response in the console for debugging purposes. In your production code, you would likely remove this.
ts_auth.pretty_print_request(prepped_request)
print(f"Response:\n{response.text}\n")