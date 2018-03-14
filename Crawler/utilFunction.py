
import requests
import time
import logging
from Crawler.User_agent import get_headers

# 验证代理是否可用测试网址
test_http_proxy_base_url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
test_https_proxy_base_url="https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"

def test_proxy (ip, type):
    if type == 'http':
        base_test_url=test_http_proxy_base_url
    elif type == 'https':
        base_test_url=test_https_proxy_base_url
    else:
        raise RuntimeError("参数错误")
    try:
        requests.get(url=base_test_url,headers=get_headers(), proxies={type: ip},timeout=2)
    except:
        print('%s connection failed ...' % ip)
        return False
    else:
        print('%s connection success...' % ip)
        return True