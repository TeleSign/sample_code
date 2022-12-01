# -*- coding: utf-8 -*-
from telesignenterprise.verify import VerifyClient
from telesign.util import random_with_n_digits
import os

# Replace the defaults below with your Telesign authentication credentials.
customer_id = os.getenv('CUSTOMER_ID', 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890')
api_key = os.getenv('API_KEY', 'TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==')

# Set the default below to your test phone number. In your production code, update the phone number dynamically for each purchase.
phone_number = os.getenv('PHONE_NUMBER', '+447975777666')

# Generate verification code.
verify_code = random_with_n_digits(5)

# Make the request and capture the response.
# If SIM Swap indicates likelihood of real fraud, verification code is not sent.
# If Score indicates likelihood of friendly fraud, verification code is not sent.
verify = VerifyClient(customer_id, api_key)
response = verify.sms(phone_number, verify_code=verify_code)

# Display the response body in the console for debugging purposes. In your production code, you would likely remove this.
print(f"\nResponse:\n{response.body}\n")

# Display prompt to enter verification code in the console.
# In your production code, you would instead collect the potential verification code from the end-user in your platform's interface.
user_entered_verify_code = input("Please enter the verification code you were sent: ")
if verify_code == user_entered_verify_code.strip():
    print("Your code is correct.")
else:
    print("Your code is incorrect.")