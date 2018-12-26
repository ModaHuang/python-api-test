import requests
import json
import yaml


def http_post(url, pattern, headers):
    req = requests.post(url, verify=False, data=pattern, headers=headers)
    return req


file = open('供應商登入p2.yaml')
test_cases = yaml.load(file)

'''
print("host = ", test_cases['host'], "type = ", type(test_cases['host']),
      "\nrest_url = ", test_cases['rest_url'], "type = ", type(test_cases['rest_url']),
      "\nuser_info = ", test_cases['user_info'], "type = ", type(test_cases['user_info']),
      "\npattern = ", test_cases['pattern'], "type = ", type(test_cases['pattern']),
      "\nheaders = ", test_cases['headers'], "type = ", type(test_cases['headers']))
'''

test_cases['url'] = test_cases['host'] + test_cases['rest_url']
# print("url = ", test_cases['url'], "type = ", type(test_cases['url']))

test_cases['pattern']['json']['email'] = test_cases['user_info']['email']
test_cases['pattern']['json']['password'] = test_cases['user_info']['password']
test_cases['pattern']['json']['deviceId'] = test_cases['user_info']['deviceId']
# print("pattern = ", test_cases['pattern'], "type = ", type(test_cases['pattern']))
test_cases_pattern = json.dumps(test_cases['pattern'])


response = http_post(test_cases['url'], test_cases_pattern, test_cases['headers'])
print('status code = ', response, '\nresponse = ', response.text)

'''
print("response = ", response, "type = ", type(response),
      "\nresponse.text = ", response.text, "type = ", type(response.text))
'''