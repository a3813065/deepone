import hmac
import hashlib
import urllib.parse
import base64
import time
import random
import json
import requests

# 默认的 OAuth 参数
DEFAULT_CONSUMER_KEY = "wPGJ2oHKUheyP6B7zg2olF9aVkOvA0HW"
DEFAULT_CONSUMER_SECRET = "GMNmyqSSOjCBSDN4IwiqmE4h6jb3Q6bsFBmDs8h4hqEcQzeGfxqPnB7jIMv18AxBiYQhCCAJBSi77GfK5cAaKNuM05MrxXZMWGayzfm5VwdLpZ3zLJlsg6JLqOiVmCzpp6iLFdsCqzfBqJiXcw0yC1PvbwaTEIExjnx4vzLmuQRS"
DEFAULT_TOKEN = "7rmLYyBI9bWDzMBXKci8cL"
DEFAULT_TOKEN_SECRET = "iCgCarpWqzYHwL7JWVvN5jfeGzrL1xDbcknARKSFarRgVEiYkPXlxNOCf59sov47Uy7JHhyLdonFs426HuubO0"
DEFAULT_USER_ID = "5Z29EGlHoYnWchaGW2TRV6"
DEFAULT_APP_VERSION = "{\"masterVersion\":\"1.235.0\",\"webVersion\":\"1.235.0\",\"apkHotUpdateVersion\":\"1.235.0\"}"

# 生成 OAuth headers，允许传入自定义参数
def generate_oauth_headers(url, method="POST", data=None, consumer_key=None, consumer_secret=None, token=None, token_secret=None, user_id=None, app_version=None):
    # 使用传入的参数或默认参数
    consumer_key = consumer_key if consumer_key not in (None, 0) else DEFAULT_CONSUMER_KEY
    consumer_secret = consumer_secret if consumer_secret not in (None, 0) else DEFAULT_CONSUMER_SECRET
    token = token if token not in (None, 0) else DEFAULT_TOKEN
    token_secret = token_secret if token_secret not in (None, 0) else DEFAULT_TOKEN_SECRET
    user_id = user_id if user_id not in (None, 0) else DEFAULT_USER_ID
    app_version = app_version if app_version not in (None, 0) else DEFAULT_APP_VERSION


    timestamp = str(int(time.time()))  # 当前的时间戳
    nonce = str(random.randint(1000000000000000, 9999999999999999))  # 随机生成 nonce

    # 请求参数
    params = {
        "oauth_token": token,
        "xoauth_requestor_id": user_id,
        "oauth_consumer_key": consumer_key,
        "oauth_signature_method": "HMAC-SHA256",
        "oauth_nonce": nonce,
        "oauth_timestamp": timestamp,
    }

    # 加入 body 参数
    if data:
        data_str = json.dumps(data)
        encoded_params = urllib.parse.urlencode(sorted(params.items()))
    else:
        encoded_params = urllib.parse.urlencode(sorted(params.items()))

    # 签名基础字符串
    base_string = f"{method.upper()}&{urllib.parse.quote(url, safe='')}"
    base_string += f"&{urllib.parse.quote(encoded_params, safe='')}"

    # 签名密钥
    key = f"{urllib.parse.quote(consumer_secret)}&{urllib.parse.quote(token_secret)}"

    # 使用 HMAC-SHA256 算法进行签名
    signature = hmac.new(key.encode(), base_string.encode(), hashlib.sha256).digest()
    oauth_signature = base64.b64encode(signature).decode()

    # Authorization 头部
    authorization_header = (
        f'OAuth realm="Users", '
        f'oauth_token="{token}", '
        f'xoauth_requestor_id="{user_id}", '
        f'oauth_consumer_key="{consumer_key}", '
        f'oauth_signature_method="HMAC-SHA256", '
        f'oauth_nonce="{nonce}", '
        f'oauth_timestamp="{timestamp}", '
        f'oauth_signature="{oauth_signature}"'
    )

    headers = {
        "accept": "application/json;charset=UTF-8",
        "accept-language": "zh-TW,zh;q=0.9",
        "authorization": authorization_header,
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-deep-one-app-version": app_version  # 使用传入的或默认的版本信息
    }

    return headers

# 发送 POST 请求
def send_post_request(url, headers, data):
    body = json.dumps(data)
    response = requests.post(url, headers=headers, data=body)

    if response.status_code == 200:
        print("Request succeeded!")
        try:
            response_json = response.json()
            print(json.dumps(response_json, ensure_ascii=False, indent=4))
        except ValueError:
            print("Failed to parse the response as JSON.")
            
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)
    return response
