import json
from getlist_and_receive import get_present_list, receive_present
from getLoginBonus import get_login_bonus
from purchase import send_purchase_request
from play import play_gacha
from refresh import get_refresh
import time
def main(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    # 这里可以定义你希望传递给 play_gacha 的自定义参数
    # 1. 先调用 getLoginBonus.py
    print("Getting Login Bonus...")
    login_response = 領取登入獎勵(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if login_response.status_code == 200:
        print("Login Bonus request succeeded!")
    else:
        print(f"Login Bonus request failed: {login_response.status_code}")

    time.sleep(1)
    # 2. 再调用 play.py
    print("Playing Gacha...")
    play_response = 刷新禮物(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if play_response.status_code == 200:
        print("Play Gacha request succeeded!")
    else:
        print(f"Play Gacha request failed: {play_response.status_code}")

    time.sleep(1)
    # 2. 再调用 refresh.py
    print("refresh...")
    refresh_response = 刷新禮物盒(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if refresh_response.status_code == 200:
        print("Play Gacha request succeeded!")
    else:
        print(f"Play Gacha request failed: {play_response.status_code}")
 
    time.sleep(1)

    # 3. 再调用 purchase.py
    print("Making first purchase with listId 3320...")
    purchase_response = 領取每日第一次(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if purchase_response is None:
        print("Purchase request failed: No response received.")

    elif purchase_response.status_code == 200:
        print("Purchase request with listId 3320 succeeded!")
    else:
        print(f"Purchase request with listId 3320 failed: {purchase_response.status_code}")

    time.sleep(1)

    # 4. 更改 listId 为 3424，发送第二次请求
    print("Making second purchase with listId 3424...")
    purchase_response = 領取每日第二次(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if purchase_response is None:
        print("Purchase request failed: No response received.")

    elif purchase_response.status_code == 200:
        print("Purchase request with listId 3424 succeeded!")
    else:
        print(f"Purchase request with listId 3424 failed: {purchase_response.status_code}")

    time.sleep(1)

    # 4. 调用 get_present_list() 获取 presentCds
    print("Getting Present List...")
    present_cds = 獲取禮物表(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    time.sleep(1)
    
    if not present_cds:
        print("No presents to receive.")
        return
    
    print(f"Present CDs to receive: {', '.join(present_cds)}")
    
    # 5. 调用 receive_present() 接收礼物
    接收禮物(consumer_key, consumer_secret, token, token_secret, user_id, app_version, present_cds)

    time.sleep(1)



    

def 獲取禮物表(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    present_cds = get_present_list(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
    )
    
    return present_cds

def 刷新禮物(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    play_response = play_gacha(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
    )
    
    return play_response

def 領取登入獎勵(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    login_response = get_login_bonus(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
    )
    
    return login_response

def 刷新禮物盒(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    refresh_response = get_refresh(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
    )
    
    return refresh_response

def 領取每日第二次(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    purchase_response = send_purchase_request(
        3424,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
    )
    
    return purchase_response

def 領取每日第一次(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    purchase_response = send_purchase_request(
        3320,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
        )
        
    return purchase_response

def 接收禮物(consumer_key, consumer_secret, token, token_secret, user_id, app_version, present_cds):
    print("Receiving Presents...")
    receive_response = receive_present(
        present_cds,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
        )
    
    if receive_response:
        print("Receive Presents request succeeded!")
        print(json.dumps(receive_response, ensure_ascii=False, indent=4))
    else:
        print("Receive Presents request failed.")
        

if __name__ == "__main__":
    main()
