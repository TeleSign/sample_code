import requests
from random import SystemRandom

def random_with_n_digits(n):
    """
    Helper function to generate a random number n digits in length using a system random.
    """
    return "".join(SystemRandom().choice('123456789') for _ in range(n))



customer_id = "526BA080-5963-4978-839A-71A5FF443B75"
api_key = "t5bQ6g7ezFMcSrT4sZ5FCr7/xtJXmjZ98SkonDS4KaJHjJKUTM5RA1vKcIkybF2iHGruEBgey81VzxccU08q1g=="

domain = "https://rest-ww.telesign.com"
endpoint = "/v1/verify/sms"
url = domain + endpoint

phone_number = "16262026728"
verify_code = random_with_n_digits(5)

headers = {
	"Authorization": "Basic NTI2QkEwODAtNTk2My00OTc4LTgzOUEtNzFBNUZGNDQzQjc1OnQ1YlE2ZzdlekZNY1NyVDRzWjVGQ3I3L3h0Slhtalo5OFNrb25EUzRLYUpIakpLVVRNNVJBMXZLY0lreWJGMmlIR3J1RUJnZXk4MVZ6eGNjVTA4cTFnPT0=",
	"Content-Type":"application/x-www-form-urlencoded"
}

payload = "phone_number=" + phone_number + "&verify_code=" + verify_code

response = requests.post(url, headers=headers, data=payload)

print("\nResponse:\n")
print(response.text)
print("\n")

user_entered_verify_code = input("Please enter the verification code you were sent: ")

if verify_code == user_entered_verify_code.strip():
    print("Your code is correct.")
else:
    print("Your code is incorrect.")