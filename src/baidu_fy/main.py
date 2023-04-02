import json

import execjs
import requests


def get_sign(param):
    node = execjs.get()
    with open('sign.js', encoding='utf-8') as f:
        js_code = f.read()
    ctx = node.compile(js_code)
    sign = ctx.call("getSign", param)
    return sign


def spider(msg, f_enc, t_enc):
    headers = {
            "Accept"            : "*/*",
            "Accept-Language"   : "zh-CN,zh;q=0.9,en;q=0.8,ar;q=0.7,ru;q=0.6",
            "Acs-Token"         : "1680423314187_1680423320982_jX/xJPBA6CVX/r3/vzf23NK1f+y26Adg6GJtMnPY3lgfUkZ6F1/iuXMIuKqi0Pti6kpTtCFc0d3V+SWLdh8rXezYcxHlqlFbqbO4iX1/8+dBcVlfK/apSUm3SjTNF4IMYIqb7gRqqeq/qKQfeAVa98m+uKBhvGol3mTa4AboAVF4kgMEMfrGMkdzB+ZhOzM1wGNIpwJ/g/tVU+cG9P9jTv7Oz0cN7/MtQjqC9htMypjqDoIlNN7bGGiB/fCu9joZPi9Xeim+q6+dJ3Z8/Ff0sa+0VAYipFr3ILparzYEhmJdfQLyeIUZzXfsndj5BGrulQZtExUOWpfZuMp9Tc1EUOEfQFUvC3Ux+MN1KMGocis4KAXZaSmIT2Q65e0VP5jPcLNLTVjbCka28pLSit0RmL16Nw5L2n50IpqbqnFfeGhliV9hYy/scWYxbbS20J1Xd94MTrjb6NkK79esGh3SNB+/DJ/IzV8X6iFTNV75H8aaVLhtxd1vtma1Tj7d/v4o",
            "Cache-Control"     : "no-cache",
            "Connection"        : "keep-alive",
            "Content-Type"      : "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin"            : "https://fanyi.baidu.com",
            "Pragma"            : "no-cache",
            "Referer"           : "https://fanyi.baidu.com/",
            "Sec-Fetch-Dest"    : "empty",
            "Sec-Fetch-Mode"    : "cors",
            "Sec-Fetch-Site"    : "same-origin",
            "User-Agent"        : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "X-Requested-With"  : "XMLHttpRequest",
            "sec-ch-ua"         : "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
            "sec-ch-ua-mobile"  : "?0",
            "sec-ch-ua-platform": "\"macOS\""
    }
    cookies = {
            "BIDUPSID"                                : "719E2A797AF746641FC0A5122FF60E95",
            "PSTM"                                    : "1632744805",
            "__yjs_duid"                              : "1_bd799c90dab65105c131010f7c8cebb91632745642833",
            "REALTIME_TRANS_SWITCH"                   : "1",
            "FANYI_WORD_SWITCH"                       : "1",
            "HISTORY_SWITCH"                          : "1",
            "SOUND_SPD_SWITCH"                        : "1",
            "SOUND_PREFER_SWITCH"                     : "1",
            "APPGUIDE_10_0_2"                         : "1",
            "MCITY"                                   : "-218%3A131%3A",
            "BAIDUID"                                 : "339AFBCEE87A42004B2E898F1E2F1084:FG=1",
            "H_WISE_SIDS"                             : "110085_188749_194530_204907_205168_209307_209568_211986_212295_212869_213030_213361_214806_215730_216842_216942_219412_219742_219943_219946_220014_221679_221874_222298_222397_222522_222625_223064_223209_224048_224077_224156_224436_224458_224573_225592_225860_226275_226548_226601_226628_226945_226965_227151_227266_227514_227528_227746_227865_227932_227971_228257_228786_229061_229080_229154_229239_229365_229379_229685_229914_229976_230084_230173_230213_230240_230248_230573_230583_230622_230685_230846_230873_230925_230930_231214_231464_231654_231722_231758_231833_231906_231978_232247_232254_232281_232356_232451_232641_232651",
            "H_WISE_SIDS_BFESS"                       : "110085_188749_194530_204907_205168_209307_209568_211986_212295_212869_213030_213361_214806_215730_216842_216942_219412_219742_219943_219946_220014_221679_221874_222298_222397_222522_222625_223064_223209_224048_224077_224156_224436_224458_224573_225592_225860_226275_226548_226601_226628_226945_226965_227151_227266_227514_227528_227746_227865_227932_227971_228257_228786_229061_229080_229154_229239_229365_229379_229685_229914_229976_230084_230173_230213_230240_230248_230573_230583_230622_230685_230846_230873_230925_230930_231214_231464_231654_231722_231758_231833_231906_231978_232247_232254_232281_232356_232451_232641_232651",
            "BDUSS"                                   : "V1YjYxNE9BeTN-MTBzRDRScEs2Z3BPWC05dXJENmU5TndSZDJvV0dtNHFYeFJrRVFBQUFBJCQAAAAAAAAAAAEAAAATo0NYcGVyamluZwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACrS7GMq0uxjQT",
            "BDUSS_BFESS"                             : "V1YjYxNE9BeTN-MTBzRDRScEs2Z3BPWC05dXJENmU5TndSZDJvV0dtNHFYeFJrRVFBQUFBJCQAAAAAAAAAAAEAAAATo0NYcGVyamluZwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACrS7GMq0uxjQT",
            "BDSFRCVID"                               : "jG-OJexroG0AahTjUneb-5Hxm7fnvd6TDYrEOwXPsp3LGJLVcXSiEG0Pt8Yk1EIbTT0MogKK0mOTHUkF_2uxOjjg8UtVJeC6EG0Ptf8g0M5",
            "H_BDCLCKID_SF"                           : "tJk8oDPbJK03fP36q4jqMJtJ5eT22jPttK39aJ5y-J7nhhjpMhO83tCqMeFtBnvLJKcXLJ-KQpbZql5pLjo0X-FRjtv7Qp52yN70Kl0MLP-WoJklQfrD3h3QXfnMBMPjamOnaU5o3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDF4jTuKe5JWjNRabK6aKC5bL6rJabC3jl0zXU6q2bDeQN3C54vn2HTX0R_EJlnWDD3IhRjfjl0vWq54WbbvLT7johRTWqR4HUnbMfonDh83ebrWJxQAKHnnop6O5hvvhb6O3M7lMUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRCD_D_y3j",
            "Hm_lvt_64ecd82404c51e03dc91cb9e8c025574" : "1680180303",
            "BDRCVFR[feWj1Vr5u3D]"                    : "I67x6TjHwwYf0",
            "delPer"                                  : "0",
            "BDSFRCVID_BFESS"                         : "jG-OJexroG0AahTjUneb-5Hxm7fnvd6TDYrEOwXPsp3LGJLVcXSiEG0Pt8Yk1EIbTT0MogKK0mOTHUkF_2uxOjjg8UtVJeC6EG0Ptf8g0M5",
            "H_BDCLCKID_SF_BFESS"                     : "tJk8oDPbJK03fP36q4jqMJtJ5eT22jPttK39aJ5y-J7nhhjpMhO83tCqMeFtBnvLJKcXLJ-KQpbZql5pLjo0X-FRjtv7Qp52yN70Kl0MLP-WoJklQfrD3h3QXfnMBMPjamOnaU5o3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDF4jTuKe5JWjNRabK6aKC5bL6rJabC3jl0zXU6q2bDeQN3C54vn2HTX0R_EJlnWDD3IhRjfjl0vWq54WbbvLT7johRTWqR4HUnbMfonDh83ebrWJxQAKHnnop6O5hvvhb6O3M7lMUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRCD_D_y3j",
            "BAIDUID_BFESS"                           : "339AFBCEE87A42004B2E898F1E2F1084:FG=1",
            "ZFY"                                     : "bhxvuLzskBOypXR4eO8I5E8x2FdZvXXO1ZtwHc0XLrY:C",
            "BA_HECTOR"                               : "ala40581ah240484ah858gcu1i2ia7q1m",
            "PSINO"                                   : "7",
            "BDORZ"                                   : "B490B5EBF6F3CD402E515D22BCDA1598",
            "H_PS_PSSID"                              : "38185_36550_38411_38113_38470_38349_38305_38468_38290_36803_38486_37919_38343_26350_38392_22160_38283_37881",
            "Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574": "1680423307",
            "ab_sr"                                   : "1.0.1_M2MwZWZmN2E1ODJiODA1Yjc3YzdjZmI2OWFhYTdiNWI1MGZhOGQ2OWRhODA3MzZhZjJiMGRlYWRmMWQ2MTQwNzE2MmY0MzFhYThjODVhNTA2YWJmZTNlNWY1YjhjY2MzYzU0ZDVmOTkwNzFkZjIyNTBhZmQ2NjRiYWE4MjkwMzQyNGFiZDA5MDA0NjM1NDY0MmEyMDgxZDA2MDlmMmU1MjQxMTM3YTBjZmM3OTFkMDdhYTNiMTg2MzJiNzA3YWRl"
    }
    url = "https://fanyi.baidu.com/v2transapi"
    params = {
            "from": f_enc,
            "to"  : t_enc,
    }
    sign = get_sign(msg)
    data = {
            "from"             : f_enc,
            "to"               : t_enc,
            "query"            : msg,
            "transtype"        : "translang",
            "simple_means_flag": "3",
            "sign"             : sign,
            "token"            : "7644715171703c3dff2db08ee4bd2527",
            "domain"           : "common"
    }
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
    k = json.loads(response.text)
    return k['trans_result']['data'][0]['dst']


if __name__ == '__main__':
    print(spider('hello', 'en', 'zh'))
    print(spider('你好', 'zh', 'en'))
