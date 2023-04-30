import json

def cca():
    import requests
    
    headers = {
            "authority"         : "www.yuque.com",
            "accept"            : "application/json",
            "accept-language"   : "zh-CN,zh;q=0.9,en;q=0.8,ar;q=0.7,ru;q=0.6",
            "cache-control"     : "no-cache",
            "content-type"      : "application/json",
            "pragma"            : "no-cache",
            "referer"           : "https://www.yuque.com/youthce/pic",
            "sec-ch-ua"         : "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
            "sec-ch-ua-mobile"  : "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest"    : "empty",
            "sec-fetch-mode"    : "cors",
            "sec-fetch-site"    : "same-origin",
            "user-agent"        : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
            "x-csrf-token"      : "7tJTN4d0Q0na29Ei7hfmnjd1",
            "x-requested-with"  : "XMLHttpRequest"
    }
    cookies = {
            "lang"          : "zh-cn",
            "yuque_ctoken"  : "7tJTN4d0Q0na29Ei7hfmnjd1",
            "_yuque_session": "qUCdVYZG416IHkxIS47HQoUOv_0C7JKrGf14epHBhAeC3qYD3rCLkUQstANT86I1o7JcV67wXyJXQnd0FZCy3A==",
            "current_theme" : "default",
            "acw_tc"        : "0b68a82a16818297159747403ec5c39d8f5b86a591a5cc71a6c9bfcd66b6fc"
    }
    url = "https://www.yuque.com/api/artboard_groups"
    params = {
            "book_id": "1797682"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    
    k = json.loads(response.text)
    k['data']
    for it in k['data']:
        name = it['name']
        import subprocess
        p = subprocess.run([
                'mkdir ./%s' % (name)],
                shell=True, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, check=False
        )
        artboards = it['artboards']
        for i,item in enumerate(artboards):
            url = item['image']
            cname = item['name']
            def download2(task, path):
                xx = task.split('.')
                localName = str(i) + "." + xx[-1]
                import subprocess
                p = subprocess.run([
                        'wget -O ./%s/%s  %s ' % (path, localName, task)],
                        shell=True, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, check=False
                )
            download2(url, name)
if __name__ == '__main__':
    cca()

