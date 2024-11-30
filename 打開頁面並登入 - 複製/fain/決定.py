import json
from fain.oauth_util import generate_oauth_headers, send_post_request

# 要发送的 API URL 和数据
def 決定Prefs(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    url = "https://tonofura-web-r.deepone-online.com/deep-one/api/gacha/decide"
    data = {

    }

    # 使用模块生成 OAuth headers
    headers = generate_oauth_headers(
        url, 
        data=data, 
        consumer_key=consumer_key, 
        consumer_secret=consumer_secret, 
        token=token, 
        token_secret=token_secret, 
        user_id=user_id, 
        app_version=app_version
    )

    # 发送请求
    response = send_post_request(url, headers, data)
    return response
