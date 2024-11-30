from fain.oauth_util import generate_oauth_headers, send_post_request
import json
# 設定 API URL 和請求數據
def updateUserNamePrefs(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    url = "https://tonofura-web-r.deepone-online.com/deep-one/api/user/updateUserName"
    data = {
        "userName": "百日紅",
        "userNameTextId": "161208648",
        "userNameStatus": "0"
    
    }

# 使用模塊生成 OAuth headers
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
# 發送 POST 請求
    response = send_post_request(url, headers, data)
    return response