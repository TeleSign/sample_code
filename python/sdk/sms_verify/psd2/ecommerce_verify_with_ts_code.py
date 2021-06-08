# -*- coding: utf-8 -*-
from telesignenterprise.verify import VerifyClient
import json


# Replace with your TeleSign authentication credentials from https://teleportal.telesign.com
customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

# Set the SMS Verify inputs. In your production code, update the phone number dynamically for each purchase.
phone_number = "+447975777666"

# Set PSD2 dynamic linking. In your production code, update these values dynamically for each purchase.
transaction_payee = "Viatu"
transaction_amount = "€40"

# Specify the language. This triggers the service to use one of our pre-written PSD2/SCA templates.
lang = "en-GB"

# Make the request and capture the response.
# If SIM Swap indicates likelihood of real fraud, verification code is not sent.
# If Score indicates likelihood of friendly fraud, verification code is not sent.
verify = VerifyClient(customer_id, api_key)
response = verify.sms(phone_number, transaction_payee=transaction_payee, transaction_amount=transaction_amount, language=lang)

# Display the response body in the console for debugging purposes. In your production code, you would likely remove this.
payload = json.loads(response.body)
print(f"\nResponse:\n{payload}\n")

# Display prompt to enter verification code in the console.
# In your production code, you would instead collect the potential verification code from the end-user in your platform's interface.
user_entered_verify_code = input("Please enter the verification code you were sent: ")
status = json.loads(verify.status(payload['reference_id'], verify_code=user_entered_verify_code).body)['verify']['code_state']
if status == 'VALID':
    print("Your code is correct.")
else:
    print("Your code is incorrect.")