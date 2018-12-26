import requests
import json

def txt_paser(fileName):
    text_file = open(fileName, "r")
    text_lines = text_file.read()
    text_lines_split = text_lines.split()
    text_url = text_lines_split[2]
    text_pattern = text_lines_split[5]
    text_headers = text_lines_split[8]
    json_text_headers = json.loads(text_headers)
    return {'url' : text_url, 'pattern' : text_pattern, 'headers' : json_text_headers}

def http_post(url, pattern, headers):
    #url = url
    #pattern = pattern
    #headers = headers
    req = requests.post(url, verify=False, data=pattern, headers=headers)
    return req

txt_paser_result = txt_paser("text_file.txt")
resp = http_post(txt_paser_result['url'], txt_paser_result['pattern'], txt_paser_result['headers'])
print('status code = ', resp, '\nresponse = ' + resp.text)

'''
method
url
pattern
headers

response
    headers
    result 
    msg

response_status
response_time

'''