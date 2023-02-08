import json
import os
import sys
import time
import requests

login_payload_string = "{\"email\":\"{{username}}\",\"password\":\"{{password}}\"}"

json_payloads = json.loads(login_payload_string)

json_payloads['email'] = "vaishali@yopmail.com"
json_payloads['password'] = "12345678"

print(json_payloads)

time.sleep(1)

file = open(sys.path[1] + os.sep + "payload_files" + os.sep + "login.json")

json_payloads_file = json.load(file)

expected_result = 'vaishali@yopmail.com'
json_payloads_file['email'] = expected_result
json_payloads_file['password'] = "12345678"
print(json_payloads_file)

url = "https://api-staging-builder.engineer.ai/users/sign_in"
headers = {"Accept": "application/json", "Content-Type": "application/json"}
print(headers)

api_response = requests.post(url=url, data=json.dumps(json_payloads_file), headers=headers)
print(api_response.content)
print(api_response.status_code)
print(api_response.elapsed.total_seconds())
print(api_response.json()['message'])

actual_result = api_response.json()['user']['email']

assert api_response.status_code == 200

assert api_response.elapsed.total_seconds() < 10

assert api_response.json()['message'] == "Signed in successfully"

assert actual_result == expected_result
