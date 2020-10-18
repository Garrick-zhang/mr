# encoding:utf-8

import requests
import base64
import json

'''
人像分割
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_seg"
# 二进制方式打开图片文件
f = open(r'D:\基于混合现实的拍摄系统\结项\测试图片\b.jpg','rb')
img = base64.b64encode(f.read())

params = {"image": img}

access_token = '24.9fb02223f036d390ef82c9e593bed340.2592000.1605004433.282335-22804541'
request_url = request_url + "?access_token=" + access_token

sss=''
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
    print(type(response.json()))
    sss=response.json()['foreground']

imagedata = base64.b64decode(sss)

file = open(r'D:\基于混合现实的拍摄系统\结项\测试图片\bc.jpg',"wb")
file.write(imagedata)
file.close()




