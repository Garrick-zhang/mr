# encoding:utf-8
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=dum3L46eAGu5sZctUr1mqmIm&client_secret=LXmGSY2paO58ByFzmnbNFsl573WZI3KZ'
response = requests.get(host)
print(1)
if response:
    print(1)
    print(response.json())
else :
    print(2)

