# import csv
# import json
# import os
# import sys
# import time
# import requests
# import pytest
#
# from test_data_driven_cases import add
#
#
# def read_data_from_csv(file_path):
#     with open(file_path, 'r') as f:
#         reader = csv.reader(f)
#         header = next(reader)
#         for item in reader:
#             yield item
#
#
# @pytest.mark.parametrize('value1,value2,expected_result', read_data_from_csv('data.csv'))
# def test_add(value1, value2, expected_result):
#     try:
#         value11= float(value1)
#     except Exception as e:
#         value11=value1
#     try:
#         value22= float(value2)
#     except Exception as e:
#         value22=value2
#     try:
#         expected_result22= float(expected_result)
#     except Exception as e:
#         expected_result22=expected_result
#     try:
#         assert add(value11, value22) == expected_result22
#     except Exception as e:
#         assert str(e) == "unsupported operand type(s) for +: 'int' and 'str'"
#
#
# @pytest.mark.parametrize('username,password,expected_status_code', read_data_from_csv('login.csv'))
# def test_login(username, password, expected_status_code):
# #    file = open(sys.path[0] + os.sep + "payload_files" + os.sep + "login.json")
#     login_payload_string = "{\"email\":\"{{username}}\",\"password\":\"{{password}}\"}"
#
#     json_payloads = json.loads(login_payload_string)
#
#     json_payloads['email'] = username
#     json_payloads['password'] = password
#
#     url = "https://api-staging-builder.engineer.ai/users/sign_in"
#     headers = {"Accept": "application/json", "Content-Type": "application/json"}
#
#     api_response = requests.post(url=url, data=json.dumps(json_payloads), headers=headers)
#
#     assert api_response.status_code == int(expected_status_code)
