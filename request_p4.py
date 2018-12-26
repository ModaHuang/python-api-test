import requests
import json
import yaml


def http_post(url, pattern, headers):
    req = requests.post(url, verify=False, data=pattern, headers=headers)
    return req


def debug(var_name, var):
    print(var_name, "=", var, "\n    type =", type(var))


file = open('供應商登入p2.yaml')
test_cases = yaml.load(file)

# for element in test_cases:
#     debug('test_cases['+element+']', test_cases[element])

test_cases['url'] = test_cases['host'] + test_cases['rest_url']


for user_info_key in test_cases['user_info']:
    # debug('user_info_key', user_info_key)
    # debug('test_cases[\'user_info\'][user_info_key]', test_cases['user_info'][user_info_key])
    test_cases['pattern']['json'][user_info_key] = test_cases['user_info'][user_info_key]
    # debug('test_cases[\'pattern\'][\'json\']['+user_info_key+']', test_cases['pattern']['json'][user_info_key])


# debug('test_cases[\'pattern\']', test_cases['pattern'])
test_cases_pattern = json.dumps(test_cases['pattern'])

resp = http_post(test_cases['url'], test_cases_pattern, test_cases['headers'])

# debug('resp.status_code', resp.status_code)
if resp.status_code == 200:
    print("PASS : response status code should be 200, status code =", resp.status_code)
else:
    print("FAIL : response status code should be 200, status code =", resp.status_code)

# debug('resp.json()', resp.json())
print('response = ', resp.text)
