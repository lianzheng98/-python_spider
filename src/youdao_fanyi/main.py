import json

import execjs


def get_sign():
    node = execjs.get()
    with open('sign.js', encoding='utf-8') as f:
        js_code = f.read()
    ctx = node.compile(js_code, cwd='../../node_modules')
    sign = ctx.call('run')
    return sign[0], sign[1]

def splider(msg):
    import requests
    headers = {
            "Accept"            : "application/json, text/plain, */*",
            "Accept-Language"   : "zh-CN,zh;q=0.9,en;q=0.8,ar;q=0.7,ru;q=0.6",
            "Cache-Control"     : "no-cache",
            "Connection"        : "keep-alive",
            "Content-Type"      : "application/x-www-form-urlencoded",
            "Origin"            : "https://fanyi.youdao.com",
            "Pragma"            : "no-cache",
            "Referer"           : "https://fanyi.youdao.com/",
            "Sec-Fetch-Dest"    : "empty",
            "Sec-Fetch-Mode"    : "cors",
            "Sec-Fetch-Site"    : "same-site",
            "User-Agent"        : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "sec-ch-ua"         : "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
            "sec-ch-ua-mobile"  : "?0",
            "sec-ch-ua-platform": "\"macOS\""
    }
    cookies = {
            "OUTFOX_SEARCH_USER_ID_NCOO": "1553104521.5236042",
            "OUTFOX_SEARCH_USER_ID"     : "\"1572866799@10.108.160.132\"",
            "_ga"                       : "GA1.2.106111151.1634375360",
            "UM_distinctid"             : "18419e87f6d29-03e84ca2e53e15-18525635-13c680-18419e87f6e6b4",
            "P_INFO"                    : "15776649676|1666882018|1|youdao_zhiyun2018|00&99|null&null&null#bej&null#10#0|&0||15776649676"
    }
    sign, mysticTime = get_sign()
    url = "https://dict.youdao.com/webtranslate"
    data = {
            "i"         : msg,
            "from"      : "auto",
            "to"        : "",
            "dictResult": "true",
            "keyid"     : "webfanyi",
            "sign"      : sign,
            "client"    : "fanyideskweb",
            "product"   : "webfanyi",
            "appVersion": "1.0.0",
            "vendor"    : "web",
            "pointParam": "client,mysticTime,product",
            "mysticTime": mysticTime,
            "keyfrom"   : "fanyi.web"
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    return response.text


def decode1(encode_txt):
    node1 = execjs.get()
    with open('decode.js', encoding='utf-8') as f:
        js_code = f.read()
    ctx = node1.compile(js_code, cwd='../../node_modules')
    text = ctx.call('run', encode_txt)
    return text


if __name__ == '__main__':
    while True:
        eng = input("输入英文:")
        res = splider(eng)
        res = json.loads(decode1(res))['dictResult']['ec']['word']['trs']
        for i in res:
            print(i)
