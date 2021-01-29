import requests
import os
import sys
    
    



# 创建目录
path = "./image/"
# 判断目录是否存在
if not os.path.exists(path):
    os.mkdir(path)
# 读入图片URL
url_list = []
with open('url.txt','r') as f:
    for line in f:
        url_list.append(list(line.strip('\n').split(',')))
# 读入图片名字，若异常，遵循默认
name_list = []
try:
    with open('name.txt','r') as f:
        for line in f:
            name_list.append(list(line.strip('\n').split(',')))
    # print(url)
except FileNotFoundError:
    for i in range(len(url_list)):
        num = i+1
        num = str(num)
        url_now = url_list[i][0]
        name_now = num
        print(url_now)
        print(name_now)
        r = requests.get(url_now)
    with open('./image/'+name_now+'.jpg', 'wb') as f:
      f.write(r.content)
    # Retrieve HTTP meta-data
    print(r.status_code)
    print(r.headers['content-type'])
    #print(r.encoding)
else:
    for i in range(len(url_list)):
        num = i+1
        num = str(num)
        url_now = url_list[i][0]
        name_now = name_list[i][0]
        print(url_now)
        print(name_now)
        r = requests.get(url_now)
        with open('./image/'+name_now+'.jpg', 'wb') as f:
          f.write(r.content)
        # Retrieve HTTP meta-data
        print(r.status_code)
        print(r.headers['content-type'])
        #print(r.encoding)
