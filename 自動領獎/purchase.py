
from oauth_util import generate_oauth_headers, send_post_request

# 定義發送請求的函數
def send_purchase_request(list_id,consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    url = "https://tonofura-web-r.deepone-online.com/deep-one/api/shop/purchase"
    data = {
        "shopId": 2,
        "listId": list_id,  # 使用動態的 listId
        "count": 1
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

    # 可以在這裡添加一些響應處理邏輯
    if response.status_code == 200:
        print(f"Purchase request with listId {list_id} succeeded!")
    else:
        print(f"Purchase request with listId {list_id} failed with status code {response.status_code}")
        print(response.text)

# 先發送一次請求，listId 為 3320




