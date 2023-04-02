import json
from datetime import datetime

import requests


class weibo:
    def __init__(self):
        self.headers = {
                "authority"         : "weibo.com",
                "accept"            : "application/json, text/plain, */*",
                "accept-language"   : "zh-CN,zh;q=0.9,en;q=0.8,ar;q=0.7,ru;q=0.6",
                "cache-control"     : "no-cache",
                "client-version"    : "v2.40.21",
                "pragma"            : "no-cache",
                "referer"           : "https://weibo.com/ershoumeigui",
                "sec-ch-ua"         : "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
                "sec-ch-ua-mobile"  : "?0",
                "sec-ch-ua-platform": "\"macOS\"",
                "sec-fetch-dest"    : "empty",
                "sec-fetch-mode"    : "cors",
                "sec-fetch-site"    : "same-origin",
                "server-version"    : "v2023.03.31.2",
                "traceparent"       : "00-a5e920e093c9b7988a6cf37cede7409d-ac892748bf970ca8-00",
                "user-agent"        : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
                "x-requested-with"  : "XMLHttpRequest",
                "x-xsrf-token"      : "VY-pGsTAsKs2dultD5HUtzb2"
        }
        
        self.cookies = {
                "XSRF-TOKEN"   : "VY-pGsTAsKs2dultD5HUtzb2",
                "SUB"          : "_2A25JLfGaDeRhGeFJ71YS9CvOyTSIHXVqW2RSrDV8PUNbmtANLWfDkW9Nf8LLMzrKFIOjQSySDcC64UzPAICd3DJ5",
                "SUBP"         : "0033WrSXqPxfM725Ws9jqgMF55529P9D9WF0W3nlS5kYuy2HEQ3eUv-h5JpX5KzhUgL.FoMNShB0Sh-Eeon2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0BXe0BfeozR",
                "ALF"          : "1711977801",
                "SSOLoginState": "1680441802",
                "WBPSESS"      : "mT-MIs9PlBvpjKs0GJfbffilBAnuzqch_rdnWEnmAfggE8zwlqELeWr9SEbB2X22nWibOK779go1VgEk7VZ70AbSRu-4XyJoGACwSpbrCCzvF2WsHMk7QizZHhPsNK1-2P7V7JMFfE75yjdKqxP-IQ==",
                "_s_tentry"    : "weibo.com",
                "Apache"       : "5057826884256.045.1680441826889",
                "SINAGLOBAL"   : "5057826884256.045.1680441826889",
                "ULV"          : "1680441826909:1:1:1:5057826884256.045.1680441826889:"
        }
        self.url = "https://weibo.com/ajax/statuses/buildComments"
        self.page = 0
        self.max_page = 1
        self.max_id = 0
    
    def work(self):
        params = {
                "flow"            : "0",
                "is_reload"       : "1",
                "id"              : "4871521942898012",  # 文件id
                "is_show_bulletin": "2",
                "is_mix"          : "0",
                "max_id"          : self.max_id,
                "count"           : "20",
                "uid"             : "1801367203",
                "fetch_level"     : "0"
        }
        response = requests.get(self.url, headers=self.headers, cookies=self.cookies, params=params)
        m = json.loads(response.text)
        ext = []
        for item in m['data']:
            tmp = {}
            tmp['用户ID'] = item['user']['id']
            tmp['用户名'] = item['user']['screen_name']
            fbtime = datetime.strptime(item["created_at"], '%a %b %d %H:%M:%S +0800 %Y')
            tmp['发布时间'] = str(fbtime)
            tmp['评论内容'] = (item['text'])
            ext.append(tmp)
        with open('a.log', 'a', encoding='utf-8') as f:
            for item in ext:
                f.write(json.dumps(item, indent=2, ensure_ascii=False))
                f.write(',')
        self.max_id = m['max_id']
        self.page += 1
        if self.page <= self.max_page:
            self.work()

a = weibo()
a.work()
