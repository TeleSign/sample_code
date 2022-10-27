from requests import Request, Session
import os
import sys

sys.path.append('../shared/')
import ts_auth

# Replace the defaults below with your Telesign authentication credentials from https://teleportal.telesign.com
customer_id = os.getenv('CUSTOMER_ID', 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890')
api_key = os.getenv('API_KEY', 'TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==')

# Set the REST API URL
url = "https://rest-ww.telesign.com/v1/phone_numbers/numbers"

# Add all headers except auth headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Date': ts_auth.format_current_date()
}

# Create session and prepped request
s = Session()
req = Request('GET', url, headers=headers)
prepped_request = req.prepare()

# Add auth to prepped request
request_properties = {
    "method": prepped_request.method,
    "headers": prepped_request.headers,
    "url": prepped_request.url
}

# prepped_request.headers = ts_auth.add_basic(request_properties, customer_id, api_key)
prepped_request.headers = ts_auth.add_digest(request_properties, customer_id, api_key)

# Make the request and capture the response.
response = s.send(prepped_request)

# Display the request and response in the console for debugging purposes. In your production code, you would likely remove this.
ts_auth.pretty_print_request(prepped_request)
print(f"Response:\n{response.text}\n")
