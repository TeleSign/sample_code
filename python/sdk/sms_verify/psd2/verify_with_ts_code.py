# -*- coding: utf-8 -*-
import os

from telesignenterprise.verify import VerifyClient


# Replace the defaults below with your TeleSign authentication credentials from https://teleportal.telesign.com
customer_id = os.getenv('CUSTOMER_ID', 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890')
api_key = os.getenv('API_KEY', 'ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==')

# Set the default below to your test phone number. In your production code, update the phone number dynamically for each purchase.
phone_number = os.getenv('PHONE_NUMBER', '+447975777666')

# Set PSD2 dynamic linking. In your production code, update these values dynamically for each purchase.
transaction_payee = "Viatu"
transaction_amount = "40 pounds"

# Specify the language. This triggers the service to use the relevant pre-written PSD2/SCA templates. By default the service uses the American English template.
lang = "en-GB"

# Make the request and capture the response.
# If SIM Swap indicates likelihood of real fraud, verification code is not sent.
# If Verify Plus indicates likelihood of friendly fraud, verification code is not sent.
verify = VerifyClient(customer_id, api_key)
response = verify.sms(phone_number, transaction_payee=transaction_payee, transaction_amount=transaction_amount, language=lang)

# Display the response body in the console for debugging purposes. In your production code, you would likely remove this.
print(f"\nResponse:\n{response.body}\n")

# Display prompt to enter verification code in the console.
# In your production code, you would instead collect the potential verification code from the end-user in your platform's interface.
user_entered_verify_code = input("Please enter the verification code you were sent: ")
status = verify.status(response.json['reference_id'], verify_code=user_entered_verify_code).json['verify']['code_state']
if status == 'VALID':
    print("Your code is correct.")
else:
    print("Your code is incorrect.")