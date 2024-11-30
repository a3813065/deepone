import json
from fain.getlist_and_receive import get_present_list, receive_present
from fain.updateUserPrefs import updateUserPrefs
from fain.purchase import send_purchase_request
from fain.play import play_gacha
from fain.決定 import 決定Prefs
from fain.refresh import get_refresh
from fain.updateUserName import updateUserNamePrefs
from fain.update.updateTutorialStep1 import updateTutorialStep1Prefs
from fain.update.updateTutorialStep2 import updateTutorialStep2Prefs
from fain.update.updateTutorialStep3 import updateTutorialStep3Prefs
from fain.update.updateTutorialStep4 import updateTutorialStep4Prefs
from fain.update.updateTutorialStep5 import updateTutorialStep5Prefs
from fain.update.updateTutorialStep6 import updateTutorialStep6Prefs
from fain.update.updateTutorialStep7 import updateTutorialStep7Prefs
from fain.update.updateTutorialStep8 import updateTutorialStep8Prefs
from fain.getLoginBonus import get_login_bonus
import time
def main(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    # 这里可以定义你希望传递给 play_gacha 的自定义参数
    # 先更新使用者訊息
    print("Getting Login Bonus...")
    updateUser_response = 更新使用者訊息(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if updateUser_response.status_code == 200:
        print("Login Bonus request succeeded!")
    else:
        print(f"Login Bonus request failed: {updateUser_response.status_code}")

    time.sleep(5)
    # 更新用戶名
    updateUserName_response = 更新名字(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if updateUserName_response.status_code == 200:
        print("Login Bonus request succeeded!")
    else:
        print(f"Login Bonus request failed: {updateUserName_response.status_code}")
 
    time.sleep(5)
    # 教程1跳過
    updateTutorialStep1_response = 教程1跳過(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if updateTutorialStep1_response.status_code == 200:
        print("教程1跳過成功")
    else:
        print(f"教程1跳過失敗: {updateTutorialStep1_response.status_code}")

    time.sleep(5)
     # 教程2跳過
    updateTutorialStep2_response = 教程2跳過(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if updateTutorialStep2_response.status_code == 200:
        print("教程2跳過成功")
    else:
        print(f"教程2跳過失敗: {updateTutorialStep2_response.status_code}")

    time.sleep(5)
     # 教程3跳過
    updateTutorialStep3_response = 教程3跳過(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if updateTutorialStep3_response.status_code == 200:
        print("教程3跳過成功")
    else:
        print(f"教程3跳過失敗: {updateTutorialStep3_response.status_code}")

    time.sleep(5)
     # 教程4跳過
    updateTutorialStep4_response = 教程4跳過(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if updateTutorialStep4_response.status_code == 200:
        print("教程4跳過成功")
    else:
        print(f"教程4跳過失敗: {updateTutorialStep4_response.status_code}")

    time.sleep(5)
     # 教程5跳過
    updateTutorialStep5_response = 教程5跳過(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if updateTutorialStep5_response.status_code == 200:
        print("教程5跳過成功")
    else:
        print(f"教程5跳過失敗: {updateTutorialStep5_response.status_code}")

    time.sleep(5)

    # 刷新禮物
    print("刷新禮物...")
    play_response = 刷新禮物(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if play_response.status_code == 200:
        print("刷新禮物成功")
    else:
        print(f"刷新禮物失敗: {play_response.status_code}")

     # 教程6跳過
    updateTutorialStep6_response = 教程6跳過(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if updateTutorialStep6_response.status_code == 200:
        print("教程6跳過成功")
    else:
        print(f"教程6跳過失敗: {updateTutorialStep6_response.status_code}")

    time.sleep(5)
    決定_response = 決定(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if 決定_response.status_code == 200:
        print("決定抽獎")
    else:
        print(f"決定失敗: {決定_response.status_code}")

    time.sleep(5)
    # 教程7跳過
    updateTutorialStep7_response = 教程7跳過(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if updateTutorialStep7_response.status_code == 200:
        print("教程7跳過成功")
    else:
        print(f"教程7跳過失敗: {updateTutorialStep7_response.status_code}")

    time.sleep(1)
    # 教程8跳過
    updateTutorialStep8_response = 教程8跳過(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if updateTutorialStep8_response.status_code == 200:
        print("教程8跳過成功")
    else:
        print(f"教程8跳過失敗: {updateTutorialStep8_response.status_code}")

    time.sleep(1)
    # 領取登入獎勵
    print("領取登入獎勵...")
    login_response = 領取登入獎勵(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if login_response.status_code == 200:
        print("領取登入獎勵成功")
    else:
        print(f"領取登入獎勵 失敗: {login_response.status_code}")

    time.sleep(1)
    # 刷新禮物盒第一次
    print("刷新禮物盒...")
    refresh_response = 刷新禮物盒(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if refresh_response.status_code == 200:
        print("刷新禮物盒 成功")
    else:
        print(f"刷新禮物盒失敗: {play_response.status_code}")

    time.sleep(1)
    # 領取購買每日1
    print("Making first purchase with listId 3320...")
    purchase_response = 領取每日第一次(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if purchase_response is None:
        print("Purchase request failed: No response received.")

    elif purchase_response.status_code == 200:
        print("Purchase request with listId 3320 succeeded!")
    else:
        print(f"Purchase request with listId 3320 failed: {purchase_response.status_code}")

    time.sleep(1)
    # 領取購買每日2
    print("Making second purchase with listId 3424...")
    purchase_response = 領取每日第二次(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if purchase_response is None:
        print("Purchase request failed: No response received.")

    elif purchase_response.status_code == 200:
        print("Purchase request with listId 3424 succeeded!")
    else:
        print(f"Purchase request with listId 3424 failed: {purchase_response.status_code}")

    time.sleep(1)

    

    # 獲取禮物表 第一次
    print("獲取禮物表...")
    present_cds = 獲取禮物表(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    time.sleep(1)
    
    if not present_cds:
        print("沒東西.")

    
    print(f"Present CDs to receive: {', '.join(present_cds)}")
    
    # 接收禮物 第一次
    接收禮物(consumer_key, consumer_secret, token, token_secret, user_id, app_version, present_cds)

    time.sleep(1)
    # 刷新禮物盒第二次
    print("刷新禮物盒...")
    refresh_response = 刷新禮物盒(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    if refresh_response.status_code == 200:
        print("刷新禮物盒 成功")
    else:
        print(f"刷新禮物盒失敗: {play_response.status_code}")

    time.sleep(1)
    # 獲取禮物表第二次
    print("獲取禮物表...")
    present_cds = 獲取禮物表(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
    time.sleep(1)

    
    if not present_cds:
        print("沒東西.")

    
    print(f"Present CDs to receive: {', '.join(present_cds)}")
    
    # 接收禮物第二次
    接收禮物(consumer_key, consumer_secret, token, token_secret, user_id, app_version, present_cds)

    time.sleep(1)




    


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

def 更新使用者訊息(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    
    updateUser_response = updateUserPrefs(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
    )
    
    return updateUser_response


def 更新名字(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    
    updateUserName_response = updateUserNamePrefs(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
    )
    
    return updateUserName_response


def 教程1跳過(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    
    updateTutorialStep1_response = updateTutorialStep1Prefs(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
    )
    
    return updateTutorialStep1_response

def 決定(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    
    決定_response = 決定Prefs(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
    )
    
    return 決定_response

def 教程2跳過(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    
    updateTutorialStep2_response = updateTutorialStep2Prefs(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
    )
    
    return updateTutorialStep2_response


def 教程3跳過(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    
    updateTutorialStep3_response = updateTutorialStep3Prefs(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
    )
    
    return updateTutorialStep3_response

def 教程4跳過(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    
    updateTutorialStep4_response = updateTutorialStep4Prefs(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
    )
    
    return updateTutorialStep4_response
def 教程5跳過(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    
    updateTutorialStep5_response = updateTutorialStep5Prefs(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
    )
    
    return updateTutorialStep5_response
def 教程6跳過(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    
    updateTutorialStep6_response = updateTutorialStep6Prefs(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
    )
    
    return updateTutorialStep6_response
def 教程7跳過(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    
    updateTutorialStep7_response = updateTutorialStep7Prefs(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
    )
    
    return updateTutorialStep7_response
def 教程8跳過(consumer_key, consumer_secret, token, token_secret, user_id, app_version):
    
    updateTutorialStep8_response = updateTutorialStep8Prefs(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        token=token,
        token_secret=token_secret,
        user_id=user_id,
        app_version=app_version
    )
    
    return updateTutorialStep8_response

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
