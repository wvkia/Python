import requests
import random
from bs4 import BeautifulSoup
import os
import time
#解析url
from Crawler.User_agent import get_headers
from Crawler.FreeProxy import GetFreeProxy

def get_proxies ():
    proxies = {
        'http': random.choice(GetFreeProxy.get_http_proxy()),
    }
    return proxies

def save_img(url):
    dir_root="G:\pircture\\"
    isExists=os.path.exists(dir_root)
    if not isExists:
        os.mkdir(dir_root)
    response=requests.get(url=url,headers=get_headers())
    file_name=str(time.time())+ os.path.splitext(url)[1]
    with open(dir_root+file_name,"wb") as f:
        f.write(response.content)

def parse_meizitu(url):
    response=requests.get(url=url,headers=get_headers())
    soup=BeautifulSoup(response.content,"html.parser")
    jpg_tags=soup.find_all("img")
    for tag in jpg_tags:
        jpg_url=tag.get("src")
        save_img(jpg_url)

def get_last_five():
    urls=["http://www.meizitu.com/a/more_"+str(x)+".html" for x in range(5)]
    return urls

if __name__ == '__main__':
    urls=get_last_five()
    for url in urls:
        parse_meizitu(url)