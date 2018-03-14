import requests
import re
from Crawler.User_agent import get_headers
from bs4 import BeautifulSoup
from Crawler.utilFunction import test_proxy
HTTPS="https"
HTTP="http"


def get_html_sp (url):
    resp = requests.get(url,headers=get_headers())
    if resp:
        return BeautifulSoup(resp.content,"html.parser")

def get_response(url):
    return requests.get(url,headers=get_headers())

class GetFreeProxy(object):
    def __init__(self):
        pass

    @staticmethod
    def freeProxyFirst():
        """
        抓取无忧代理 http://www.data5u.com/
        :return:
        """
        def get_urls(url):
            html_rep=get_html_sp(url)
            url_l2_list=html_rep.find_all(class_="l2")
            urls=[]
            for url_l2 in url_l2_list:
                try:
                    url_li=url_l2.find_all("li")
                    urls.append(url_li[0].text+":"+url_li[1].text)
                except Exception as e :
                    print(e)
            return urls
        url_dict={}
        url_dict[HTTP]=get_urls("http://www.data5u.com/free/type/http/index.html")
        url_dict[HTTPS]=get_urls("http://www.data5u.com/free/type/https/index.html")
        return url_dict

    @staticmethod
    def freeProxySecond():
        """
        抓取66代理 http://www.66ip.cn/
        :return:
        """
        def get_urls(type,number=20):
            proxy_type=1
            if type == HTTPS:
                proxy_type=1
            if type==HTTP:
                proxy_type=0
            url="http://www.66ip.cn/nmtq.php?getnum="+str(number)+"&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=1&proxytype="+str(proxy_type)+"&api=66ip"
            html=get_html_sp(url)
            urls=[]
            #正则匹配，并且提取内容以gbk解码
            for url in re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}',html.decode("gbk")):
                urls.append(url)
            return urls
        urls_dict={}
        urls_dict[HTTP]=get_urls(type=HTTP)
        urls_dict[HTTPS]=get_urls(type=HTTPS)
        return urls_dict

    @staticmethod
    def freeProxyThird():
        """
        抓取IP181 http://www.ip181.com/
        :return:
        """
        url="http://www.ip181.com/"
        html_resp=get_html_sp(url)
        url_dict={HTTP:[],HTTPS:[]}
        try:
            tr_list=html_resp.find_all("tr")[1:]
            for tr in tr_list:
                tds=tr.find_all("td")
                ip=tds[0].text+":"+tds[1].text
                protocal=tds[3].text
                if HTTP in protocal.lower():
                    url_dict.get(HTTP).append(ip)
                if HTTPS in protocal.lower():
                    url_dict.get(HTTPS).append(ip)
        except Exception as e:
            print(e)
        return url_dict

    @staticmethod
    def freeProxyFourth():
        """
        西刺代理 http://www.xicidaili.com/nn/
        :return:
        """
        pass


    @staticmethod
    def freeProxyXun():
        """
        抓取讯代理 http://www.xdaili.cn/ipagent/freeip/getFreeIps?page=1&rows=10
        :return:
        """
        url="http://www.xdaili.cn/ipagent/freeip/getFreeIps?page=1&rows=10"
        url_dict={HTTP:[],HTTPS:[]}
        try:
            json_=get_response(url).json()
            for row in json_['RESULT']['rows']:
                ip='{ip}:{port}'.format(row['ip'],row['port'])
                if HTTP in row['type'].lower():
                    url_dict.get(HTTP).append(ip)
                if HTTPS in row['type'].lower():
                    url_dict.get(HTTPS).append(ip)
        except Exception as e:
            print(e)
        return url_dict

    @staticmethod
    def proxy_method_arr():
        return [GetFreeProxy.freeProxyFirst(),GetFreeProxy.freeProxySecond(),GetFreeProxy.freeProxyThird(),GetFreeProxy.freeProxyXun()]


    @staticmethod
    def get_free_proxy():
        """
        获取通过测试的代理ip
        :return:
        """
        proxy_method_arr =(GetFreeProxy.freeProxyFirst(),GetFreeProxy.freeProxySecond(),GetFreeProxy.freeProxyThird(),GetFreeProxy.freeProxyXun())

        url_dict={HTTP:[],HTTPS:[]}
        for dict_ in proxy_method_arr:


            for k,v in dict_.items():
                if k and v:
                    if k == HTTP:
                        if len(url_dict.get(k)) > 10:
                            continue
                        for ip in v:
                            if test_proxy(ip,k):
                                url_dict.get(k).append(ip)
                    if k == HTTPS:
                        if len(url_dict.get(k)) > 10:
                            continue
                        for ip in v:
                            if test_proxy(ip,k):
                                url_dict.get(k).append(ip)
                if len(url_dict.get(HTTP)) > 10 and len(url_dict.get(HTTPS)) > 10:
                    return url_dict
        return url_dict


    @staticmethod
    def get_http_proxy():
        urls=[]
        proxy_method_arr =(GetFreeProxy.freeProxyFirst(),GetFreeProxy.freeProxySecond(),GetFreeProxy.freeProxyThird(),GetFreeProxy.freeProxyXun())
        for dict_prox in proxy_method_arr:
            for k,v in dict_prox.items():
                if k == HTTP:
                    for ip in v:
                        urls.append(ip)
                        if len(urls) > 10:
                            return urls

        return urls



if __name__ == '__main__':
    # for k,v in GetFreeProxy.freeProxyThird().items():
    #     print(k," ",v)
    gg=GetFreeProxy
    gg.get_free_proxy()
