import requests
import urllib.request
import uuid
from bs4 import BeautifulSoup
import os

if os.path.exists('D:\Bing_image') == True:  # 如果目录不存在则创建
    print("image dir is exsit")
else:
    os.mkdir('image')
i = 0
img_list =  []
for page in range(1,5):
    url = 'https://bing.ioliu.cn/?p='+str(page)
    #print(url)
    r = requests.get(url)
    contents = r.text

    soup = BeautifulSoup(contents,'html.parser')
    divs = soup.find_all('div','item')

    for div in divs:
        imgs = div.find_all('img')
        for img in imgs:
            print(img['src'].replace('320x240','1920x1080'))
            img_list.append("\"" + img['src'].replace('320x240','1920x1080') + "\"" + ",")
            # urllib.request.urlretrieve(img['src'].replace('320x240','1920x1080'),'D:\Bing_image\%s.jpg'%i)
            i += 1
            print('成功抓取第%s张图片'%i)
print('共抓取'+str(i)+'张图片')


FileOject = open('D:\Bing_image\img.txt', 'w')
for img in img_list:
    FileOject.write(img)
    FileOject.write('\n')


print("Done!")