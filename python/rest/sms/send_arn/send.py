import os
import requests
import sys
sys.path.append('../../shared/')
import ts_auth
import ts_utils


# Set the REST API URL
base_url = "https://rest-ww.telesign.com/v1/messaging"

# Set the SMS API inputs. In your production code, update the phone number dynamically for each purchase.
# Set the default below to your test phone number. In your production code, update the phone number dynamically for each purchase.
phone_number = os.getenv('PHONE_NUMBER', '15551212')

# Provide message details and description for the payload
message = "Your message here."
message_type = "ARN"

# Set request headers
headers = {
	"Content-Type":"application/x-www-form-urlencoded"
}
# Add auth headers. Use one of the two statements below that matches your desired auth method.
ts_auth.add_basic(headers)
#ts_auth.add_digest(headers)

# Create the payload
payload = f"phone_number={phone_number}&message={message}&message_type={message_type}"

# Make the request and capture the response.
response = requests.post(base_url, headers=headers, data=payload.encode('utf-8'))
prepped_request = ts_utils.format_prepped_request(response.request, 'utf8')

# Display the request and response in the console for debugging purposes. In your production code, you would likely remove this.
print(f"\nRequest:\n{prepped_request}\n\nResponse:\n{response.text}\n")
