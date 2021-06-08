import requests
import hmac
from hashlib import sha256
from base64 import b64encode, b64decode
from random import SystemRandom
import datetime
import pytz

def random_with_n_digits(n):
    # Helper function to generate a random number n digits in length using a system random.
    return "".join(SystemRandom().choice('123456789') for _ in range(n))

def pretty_print_POST(req):
    # Previews the prepared request.
    print('{}\r\n{}\r\n\r\n{}'.format(
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

def create_timestamp():
	# Creates a timestamp for "now" that is timezone-aware (UTC +000).
	timestamp = pytz.utc.localize(datetime.datetime.utcnow())
	return timestamp

# Define TeleSign credentials
customer_id = "526BA080-5963-4978-839A-71A5FF443B75"
api_key = "t5bQ6g7ezFMcSrT4sZ5FCr7/xtJXmjZ98SkonDS4KaJHjJKUTM5RA1vKcIkybF2iHGruEBgey81VzxccU08q1g=="

# Define the endpoint
domain = "https://rest-ww.telesign.com"
resource = "/v1/verify/sms"
query_string = ""
url = domain + resource + query_string

# Define values for headers
timestamp = create_timestamp().strftime("%a, %d %b %Y %H:%M:%S +0000")
content_type = "application/x-www-form-urlencoded"
auth_method = "HMAC-SHA256"

# Create canonicalized TS headers
auth_method_header = "x-ts-auth-method:" + auth_method
canon_ts_headers = ""
canon_ts_headers += auth_method_header

# Create the payload
phone_number = "16262026728"
verify_code = random_with_n_digits(5)
payload = "phone_number=" + phone_number + "&verify_code=" + verify_code

# Create canonicalized POST variables
canon_post_variables = payload

# Create canonicalized resource
canon_resource = resource

# Create string to sign
str_to_sign = "POST\n"
str_to_sign += (content_type + "\n")
str_to_sign += (timestamp + "\n")
str_to_sign += (canon_ts_headers + "\n")
str_to_sign += (canon_post_variables + "\n")
str_to_sign += canon_resource

# Create signature and auth string
signer = hmac.new(b64decode(api_key), str_to_sign.encode("utf-8"), sha256)
signature = b64encode(signer.digest()).decode("utf-8")
auth_str = "TSA " + customer_id + ":" + signature
headers = {
	"Authorization": auth_str,
	"Content-Type": content_type,
	"Date": timestamp,
	"x-ts-auth-method": auth_method
}

# Prepare the request
prepared_req = requests.Request('POST', url, headers=headers, data=payload).prepare()

# Print a preview of the request
print("\nRequest:")
pretty_print_POST(prepared_req)

# Make the request
response = requests.post(url, headers=headers, data=payload)

# Print the response
print("\nResponse:")
print(response.text)

# Verify
user_entered_verify_code = input("Please enter the verification code you were sent: ")
if verify_code == user_entered_verify_code.strip():
    print("Your code is correct.\n")
else:
   print("Your code is incorrect.\n")