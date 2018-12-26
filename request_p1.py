import requests
import json

def http_post():
    url = 'https://api-203.sit.kkday.com/api/supplier/login'
    pattern = {"apiKey":"kkdayapi","userOid":"1","ver":"1.0.1","locale":"zh-tw","ipaddress":"127.0.0.1","json":{"deviceId":"05d796cc451187682e4daa696b2b8759","email":"moda.huang@kkday.com","password":"123456","ipaddress":"0.0.0.0"}}
    headers = {'Content-Type' : 'application/json'}
    jdata = json.dumps(pattern)
    req = requests.post(url, verify=False, data=jdata,headers=headers)
    print(req,"\n",req.text)
    #print(req, "\n")

#resp = http_post()
http_post()

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