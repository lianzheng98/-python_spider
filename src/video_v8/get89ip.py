from collections import namedtuple
from multiprocessing import Pool

import requests
from lxml import etree

ipCls = namedtuple('ipCls', 'ip,port,di,ct,ti,flag')


class Get89Ip:
    def __init__(self, f, e):
        self.f = f
        self.e = e
    
    def generateUrls(self):
        self.urls = [f"https://www.89ip.cn/index_{p}.html" for p in range(f, e + 1)]
    
    def getHtml(self, url):
        try:
            headers = {
                    "Accept"                   : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "Accept-Language"          : "zh-CN,zh;q=0.9,en;q=0.8,ar;q=0.7,ru;q=0.6",
                    "Cache-Control"            : "no-cache",
                    "Connection"               : "keep-alive",
                    "Pragma"                   : "no-cache",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent"               : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
            }
            res = requests.get(url, headers=headers)
            html = etree.HTML(res.text)
            arr = [i.strip() for i in html.xpath('//tr/td/text()')]
            ci = []
            for i in range(0, len(arr), 5):
                ip = arr[i]
                port = arr[i + 1]
                di = arr[i + 2]
                ct = arr[i + 3]
                ti = arr[i + 4]
                
                a = ipCls(ip=ip, port=port, di=di, ct=ct, ti=ti, flag=False)
                ci.append(a)
            return ci
        except Exception:
            return []
    
    def getCheck(self, ip_item):
        try:
            ip_a_port = 'http://{ip}:{port}'.format(ip=ip_item.ip, port=ip_item.port)
            res = requests.get('http://httpbin.org/ip', headers={
                    "Accept"                   : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "Accept-Language"          : "zh-CN,zh;q=0.9,en;q=0.8,ar;q=0.7,ru;q=0.6",
                    "Cache-Control"            : "no-cache",
                    "Connection"               : "keep-alive",
                    "Pragma"                   : "no-cache",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent"               : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
            }, proxies={'http': ip_a_port},
                               timeout=2,
                               verify=False
                               )
            print(res.text)
            if res.status_code == 200:
                print('IP可用-->', ip_a_port)
                return ip_item
        except Exception:
            return None
    
    def run(self):
        self.generateUrls()
        pool = Pool(processes=2)
        urls = self.urls
        ci = pool.map(self.getHtml, urls)
        ci = [it for arr in ci for it in arr]
        
        reci = pool.map(self.getCheck, ci)
        print(len(reci))
        farr = list(filter(lambda x: x is not None, reci))
        print(len(farr))
        print(farr)


if __name__ == '__main__':
    f = 3
    e = 3
    work = Get89Ip(f, e)
    work.run()
