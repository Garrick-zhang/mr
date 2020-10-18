#保存图片
import base64
import urllib
import json
import requests


def save_base_image(img_str,filename):
    img_data = base64.b64decode(img_str)
    with open(filename, 'wb') as f:
          f.write(img_data)

     
#人像分割
#filename:原图片名（本地存储包括路径）；dehazedfilename:处理后的文件保存名称
def body_seg_fore(filename,resultfilename):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_seg"
    
    # 二进制方式打开图片文件
    f = open(filename, 'rb')
    img = base64.b64encode(f.read())
    
    params = {"image": img}
    #params = json.dumps(params).encode('utf-8')
    
    access_token = '24.9fb02223f036d390ef82c9e593bed340.2592000.1605004433.282335-22804541'
    request_url = request_url + "?access_token=" + access_token

    sss=''
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
       print (response.json())
       print(type(response.json()))
       sss=response.json()['foreground']
    save_base_image(sss,resultfilename)
#图片整合
#foreimage：前景照片，baseimage：景区照片,outputimage：数据结果,rate：前景照片缩放比例
def combine_image(foreimage,baseimage,outputimage,rate):
    from PIL import Image
    base_img = Image.open(baseimage)
    BL, BH = base_img.size
    #读取要粘贴的图片 RGBA模式    
    #当需要将一张有透明部分的图片粘贴到一张底片上时，如果用Python处理，可能会用到PIL，
    #但是PIL中 有说明，在粘贴RGBA模式的图片是，alpha通道不会被帖上，也就是不会有透明的效果，
    #当然也给出了解决方法，就是粘贴的时候，将RGBA的的alpha通道提取出来做为mask传入。
    fore_image = Image.open(foreimage)
    L, H = fore_image.size
    #缩放
    fore_image = fore_image.resize((int(L * rate), int(H * rate)))
    L, H = fore_image.size
    #分离通道    
    r,g,b,a = fore_image.split()    #粘贴
    
    box=(int(BL/2-L/2), BH-H, int(BL/2+L/2) ,BH)
    
    base_img.paste(fore_image,box,mask = a)
    base_img.save(outputimage)  # 保存图片
    
#输出程序
def travel_image(originimage,baseimage,outputimage,rate):
    body_seg_fore(originimage,'seg_'+originimage)
    combine_image('seg_'+originimage,baseimage,outputimage,rate)

#travel_image('crowd1.jpg','grassland.jpg','crowd1_grassland.png',0.35)
travel_image('a.jpg','lou.jpg','a_lou.png',1.7)
