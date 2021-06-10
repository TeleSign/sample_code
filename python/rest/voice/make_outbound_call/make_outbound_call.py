import base64
import requests
import os

# Replace the defaults below with your TeleSign authentication credentials from https://teleportal.telesign.com
customer_id = os.getenv('CUSTOMER_ID', 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890')
api_key = os.getenv('API_KEY', 'TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==')

# Set the REST API URL
url = "https://rest-ww.telesign.com/v2/voice"

# Set the Voice API inputs.
destination_number = os.getenv('PHONE_NUMBER', '15554441313') # The complete phone number you want to call, including country code, with no special characters or spaces.
caller_id_number = os.getenv('SENDER_ID', '15555551212') # The phone number you purchased from TeleSign.
send_dtmf = '8' # Digits to add into the call.

# Generate auth string.
auth_string = ":".join([customer_id, api_key]).encode()
auth_string = " ".join(["Basic", base64.b64encode(auth_string).decode("utf-8")])

# Create the request body.
payload = {
  "method": "dial",
  "params": {
    "to": destination_number,
    "caller_id_number": caller_id_number,
    "send_dtmf": send_dtmf
  }
}

# Create the request headers.
headers = {
  'Accept': "application/json",
  'Content-Type': "application/json",
  'Authorization': auth_string
}

# Make the request and capture the response.
response = requests.post(url, headers=headers, json=payload)

# Display the response for debugging purposes.
print(f"\nResponse:\n{response.status_code}\n")