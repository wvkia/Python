import requests
import os
import pdfkit
from bs4 import BeautifulSoup
import time
import random


#解析url
def parse_url_to_html(url,file_name):
    response=requests.get(url, headers={'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'})
    soup=BeautifulSoup(response.content,'html.parser')
    body=soup.find_all(class_="x-wiki-content x-main-content")[0]
    html=str(body).encode('utf-8')
    with open(file_name,'wb') as f:
        f.write(html)

def get_url_list():
    """
    获取所有url目录
    :return:
    """
    baseUrl='https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'
    response=requests.get(baseUrl,headers={'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'})
    soup=BeautifulSoup(response.content,'html.parser')
    print(soup)
    menu_tag=soup.find_all(class_='uk-nav uk-nav-side')[1]
    urls=[]
    for li in menu_tag.find_all('div'):
        url="http://www.liaoxuefeng.com" + li.a.get('href')
        urls.append(url)
    return urls

def save_pdf(htmls):
    """
    把html转成pdf
    :param htmls:
    :return:
    """
    options={
        'page-size': 'Letter',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ]
    }
    file_name='a.pdf'
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdfkit.from_file(htmls,file_name,options=options,configuration=config)

import datetime
if __name__ == '__main__':
    # start_url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000"
    # parse_url_to_html(start_url)
    print(get_url_list())
    urls=get_url_list()
    htmlnames=[]
    for u in urls:
        print(u)
        filename=str(int(datetime.datetime.now().timestamp()))+".html"
        parse_url_to_html(u,filename)
        #
        time.sleep(3+random.randint(0,9))
        htmlnames.append(filename)
    save_pdf(htmlnames)
    for fn in htmlnames:
        os.remove(fn)


