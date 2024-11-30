# getlist_and_receive.py
import json
from oauth_util import generate_oauth_headers, send_post_request

def get_present_list(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    # 設定 API URL 和請求數據
    url = "https://tonofura-web-r.deepone-online.com/deep-one/api/present/getList"
    data = {
        "index": 0,
        "categories": "1,2,3,4",
        "hasPeriod": 1,
        "noPeriod": 1
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

    # 處理回應
    if response.status_code == 200:
        try:
            response_json = response.json()  # 假設回應是 JSON 格式
            present_cds = [present['presentCd'] for present in response_json.get('presents', [])]
            return present_cds
        except ValueError:
            print("Failed to parse the response as JSON.")
            return []
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)
        return []

def receive_present(present_cds,consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    # 將 presentCds 轉換為逗號分隔的字符串
    present_cds_str = ",".join(present_cds)

    # 設定要發送的 API URL 和數據
    receive_url = "https://tonofura-web-r.deepone-online.com/deep-one/api/present/receive"
    receive_data = {
        "presentCds": present_cds_str,
        "receiveType": 1
    }

    # 使用模塊生成 OAuth headers
    receive_headers = generate_oauth_headers(
        receive_url, 
        data=receive_data,
        consumer_key=consumer_key, 
        consumer_secret=consumer_secret, 
        token=token, 
        token_secret=token_secret, 
        user_id=user_id, 
        app_version=app_version
        )

    # 發送請求
    receive_response = send_post_request(receive_url, receive_headers, receive_data)

    # 打印回應
    if receive_response.status_code == 200:
        try:
            receive_response_json = receive_response.json()
            return receive_response_json
        except ValueError:
            print("Failed to parse the receive response as JSON.")
            return None
    else:
        print(f"Receive request failed with status code {receive_response.status_code}")
        print(receive_response.text)
        return None

