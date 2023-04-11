import concurrent.futures
import json
import os.path

import requests


def download(task):
    try:
        ph = './src'
        d = os.path.exists(ph)
        if not d:
            os.mkdir(ph)
        
        def getName(url):
            arr = url.split('/')
            return arr[-1].split('&')[0]
        
        res = requests.get(task, headers={
                "Accept"            : "text/plain, */*; q=0.01",
                "Accept-Language"   : "zh-CN,zh;q=0.9,en;q=0.8,ar;q=0.7,ru;q=0.6",
                "Cache-Control"     : "no-cache",
                "Connection"        : "keep-alive",
                "Pragma"            : "no-cache",
                "Referer"           : "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1680444607099_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MCwzLDYsNCwxLDUsMiw3LDgsOQ%3D%3D&ie=utf-8&ctd=1680444607100%5E00_1440X150&sid=&word=%E9%BB%91%E4%B8%9D",
                "Sec-Fetch-Dest"    : "empty",
                "Sec-Fetch-Mode"    : "cors",
                "Sec-Fetch-Site"    : "same-origin",
                "User-Agent"        : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
                "X-Requested-With"  : "XMLHttpRequest",
                "sec-ch-ua"         : "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
                "sec-ch-ua-mobile"  : "?0",
                "sec-ch-ua-platform": "\"macOS\""
        }
                           )
        with open("{}/{}".format(ph, getName(task)), 'wb') as f:
            f.write(res.content)
    except Exception as e:
        print('url has problem', e)


def download2(task):
    import subprocess
    p = subprocess.run([
            'wget %s -P ./src ' % task],
            shell=True, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, check=False
    )
    print(p)


def pc(tasks, max_workers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        fs = []
        for task in tasks:
            fs.append(executor.submit(download2, task))
        for future in concurrent.futures.as_completed(fs):
            future.result()


class I:
    def __init__(self, key):
        self.key = key
        self.pn = 50
        self.rn = 50
        self.headers = {
                "Accept"            : "text/plain, */*; q=0.01",
                "Accept-Language"   : "zh-CN,zh;q=0.9,en;q=0.8,ar;q=0.7,ru;q=0.6",
                "Cache-Control"     : "no-cache",
                "Connection"        : "keep-alive",
                "Pragma"            : "no-cache",
                "Referer"           : "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1680444607099_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MCwzLDYsNCwxLDUsMiw3LDgsOQ%3D%3D&ie=utf-8&ctd=1680444607100%5E00_1440X150&sid=&word=%E9%BB%91%E4%B8%9D",
                "Sec-Fetch-Dest"    : "empty",
                "Sec-Fetch-Mode"    : "cors",
                "Sec-Fetch-Site"    : "same-origin",
                "User-Agent"        : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
                "X-Requested-With"  : "XMLHttpRequest",
                "sec-ch-ua"         : "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
                "sec-ch-ua-mobile"  : "?0",
                "sec-ch-ua-platform": "\"macOS\""
        }
        self.url = "https://image.baidu.com/search/acjson"
        self.params = {
                "tn"           : "resultjson_com",
                "logid"        : "10748773937448771767",
                "ipn"          : "rj",
                "ct"           : "201326592",
                "is"           : "",
                "fp"           : "result",
                "fr"           : "",
                "word"         : self.key,
                "queryWord"    : self.key,
                "cl"           : "2",
                "lm"           : "-1",
                "ie"           : "utf-8",
                "oe"           : "utf-8",
                "adpicid"      : "",
                "st"           : "-1",
                "z"            : "",
                "ic"           : "",
                "hd"           : "",
                "latest"       : "",
                "copyright"    : "",
                "s"            : "",
                "se"           : "",
                "tab"          : "",
                "width"        : "",
                "height"       : "",
                "face"         : "0",
                "istype"       : "2",
                "qc"           : "",
                "nc"           : "1",
                "expermode"    : "",
                "nojc"         : "",
                "isAsync"      : "",
                "pn"           : self.pn,
                "rn"           : self.rn,
                "gsm"          : "3c",
                "1680444613081": ""
        }
        self.max_size = 100
        self.urls = []
    
    def work(self):
        cookies = {
                "BDqhfp"              : "python%20__init__.py%26%26NaN-1undefined%26%2631212%26%2638",
                "BIDUPSID"            : "719E2A797AF746641FC0A5122FF60E95",
                "PSTM"                : "1632744805",
                "__yjs_duid"          : "1_bd799c90dab65105c131010f7c8cebb91632745642833",
                "MCITY"               : "-218%3A131%3A",
                "BAIDUID"             : "339AFBCEE87A42004B2E898F1E2F1084:FG=1",
                "H_WISE_SIDS"         : "110085_188749_194530_204907_205168_209307_209568_211986_212295_212869_213030_213361_214806_215730_216842_216942_219412_219742_219943_219946_220014_221679_221874_222298_222397_222522_222625_223064_223209_224048_224077_224156_224436_224458_224573_225592_225860_226275_226548_226601_226628_226945_226965_227151_227266_227514_227528_227746_227865_227932_227971_228257_228786_229061_229080_229154_229239_229365_229379_229685_229914_229976_230084_230173_230213_230240_230248_230573_230583_230622_230685_230846_230873_230925_230930_231214_231464_231654_231722_231758_231833_231906_231978_232247_232254_232281_232356_232451_232641_232651",
                "H_WISE_SIDS_BFESS"   : "110085_188749_194530_204907_205168_209307_209568_211986_212295_212869_213030_213361_214806_215730_216842_216942_219412_219742_219943_219946_220014_221679_221874_222298_222397_222522_222625_223064_223209_224048_224077_224156_224436_224458_224573_225592_225860_226275_226548_226601_226628_226945_226965_227151_227266_227514_227528_227746_227865_227932_227971_228257_228786_229061_229080_229154_229239_229365_229379_229685_229914_229976_230084_230173_230213_230240_230248_230573_230583_230622_230685_230846_230873_230925_230930_231214_231464_231654_231722_231758_231833_231906_231978_232247_232254_232281_232356_232451_232641_232651",
                "BDUSS"               : "V1YjYxNE9BeTN-MTBzRDRScEs2Z3BPWC05dXJENmU5TndSZDJvV0dtNHFYeFJrRVFBQUFBJCQAAAAAAAAAAAEAAAATo0NYcGVyamluZwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACrS7GMq0uxjQT",
                "BDUSS_BFESS"         : "V1YjYxNE9BeTN-MTBzRDRScEs2Z3BPWC05dXJENmU5TndSZDJvV0dtNHFYeFJrRVFBQUFBJCQAAAAAAAAAAAEAAAATo0NYcGVyamluZwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACrS7GMq0uxjQT",
                "BDSFRCVID"           : "jG-OJexroG0AahTjUneb-5Hxm7fnvd6TDYrEOwXPsp3LGJLVcXSiEG0Pt8Yk1EIbTT0MogKK0mOTHUkF_2uxOjjg8UtVJeC6EG0Ptf8g0M5",
                "H_BDCLCKID_SF"       : "tJk8oDPbJK03fP36q4jqMJtJ5eT22jPttK39aJ5y-J7nhhjpMhO83tCqMeFtBnvLJKcXLJ-KQpbZql5pLjo0X-FRjtv7Qp52yN70Kl0MLP-WoJklQfrD3h3QXfnMBMPjamOnaU5o3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDF4jTuKe5JWjNRabK6aKC5bL6rJabC3jl0zXU6q2bDeQN3C54vn2HTX0R_EJlnWDD3IhRjfjl0vWq54WbbvLT7johRTWqR4HUnbMfonDh83ebrWJxQAKHnnop6O5hvvhb6O3M7lMUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRCD_D_y3j",
                "BDORZ"               : "B490B5EBF6F3CD402E515D22BCDA1598",
                "BAIDUID_BFESS"       : "339AFBCEE87A42004B2E898F1E2F1084:FG=1",
                "BDSFRCVID_BFESS"     : "jG-OJexroG0AahTjUneb-5Hxm7fnvd6TDYrEOwXPsp3LGJLVcXSiEG0Pt8Yk1EIbTT0MogKK0mOTHUkF_2uxOjjg8UtVJeC6EG0Ptf8g0M5",
                "H_BDCLCKID_SF_BFESS" : "tJk8oDPbJK03fP36q4jqMJtJ5eT22jPttK39aJ5y-J7nhhjpMhO83tCqMeFtBnvLJKcXLJ-KQpbZql5pLjo0X-FRjtv7Qp52yN70Kl0MLP-WoJklQfrD3h3QXfnMBMPjamOnaU5o3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDF4jTuKe5JWjNRabK6aKC5bL6rJabC3jl0zXU6q2bDeQN3C54vn2HTX0R_EJlnWDD3IhRjfjl0vWq54WbbvLT7johRTWqR4HUnbMfonDh83ebrWJxQAKHnnop6O5hvvhb6O3M7lMUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRCD_D_y3j",
                "BA_HECTOR"           : "81258l212l252k840lak00bt1i2iud01m",
                "BDRCVFR[feWj1Vr5u3D]": "I67x6TjHwwYf0",
                "delPer"              : "0",
                "ZFY"                 : "bhxvuLzskBOypXR4eO8I5E8x2FdZvXXO1ZtwHc0XLrY:C",
                "PSINO"               : "1",
                "H_PS_PSSID"          : "38185_36550_38411_38113_38470_38349_38305_38468_38290_36803_38486_37919_38343_38356_26350_38392_22160_38283_37881",
                "BDRCVFR[dG2JNJb_ajR]": "mk3SLVN4HKm",
                "userFrom"            : "www.baidu.com",
                "BDRCVFR[-pGxjrCMryR]": "mk3SLVN4HKm",
                "indexPageSugList"    : "%5B%22%E9%BB%91%E4%B8%9D%22%5D",
                "cleanHistoryStatus"  : "0",
                "ab_sr"               : "1.0.1_OTBlOTE3YTBjNWY1YzUxZDZlMGJkOGZjNGFjYzllYzUxMDI5MjlmYzZjNjlhOGRhMGZlMTlhM2Y1NDU1MGQyMzcwMGU4NTJkMDYxMjRhOWNjNDA1OGU1ZjhkYWQwNDgzNWZiZTRmMzNmMmExODYwNmI0M2RlZmU0ZDlkMDlhNDUzNmE4MDVhMTJhODliZDYxYWEzMGJhOGY0OWFhZWU4NQ=="
        }
        url = "https://image.baidu.com/search/acjson"
        for i in range(self.max_size // self.rn):
            self.params['pn'] = self.params['rn'] * i
            response = requests.get(url, headers=self.headers, cookies=cookies, params=self.params)
            m = json.loads(response.text)
            for item in m['data']:
                if 'replaceUrl' in item:
                    for arr in item['replaceUrl']:
                        self.urls.append(arr['ObjURL'])
            print(len(self.urls))
    
    def download(self):
        pc(self.urls, 4)
    
    def run(self):
        self.urls = []
        self.work()
        print(self.urls)
        self.download()
    
    def getAllSize(self):
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            max_num = json.loads(response.text)['displayNum']
            return max_num
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # key = input('请输入一个关键词')
    # num = input('获取一个你输入的数量')
    key = '白丝'
    a = I(key)
    max_size = a.getAllSize()
    print(max_size)
    if max_size > 100:
        max_size = 100
    a.max_size = max_size
    a.run()
    
  