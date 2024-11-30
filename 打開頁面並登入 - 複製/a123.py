import os
import random
import json
from playwright.sync_api import sync_playwright
from fain.main import main
import time

import random

def generate_standard_user_agent():
    """生成一個常見且有效的 User-Agent 字串"""
    user_agents = [
        # Chrome on Windows
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36",
    ]
    return random.choice(user_agents)

def opengame(email, password, imap_server):
    """用於自動化註冊 DMM 帳戶的函數"""
    opengame_url = "https://accounts.dmm.co.jp/service/login/password/=/path=https%3A%2F%2Fgames.dmm.co.jp%2Fdetail%2Fdeeponer/channel=games"
    error_url = "https://games.dmm.co.jp/detail/deeponer"
    regist_url = "https://personal.games.dmm.co.jp/profile/regist"
    special_url = "https://play.games.dmm.co.jp/game/deeponer"
    

    註冊(email, password, opengame_url, error_url, regist_url, special_url)
    


    




def 註冊(email, password, opengame_url, error_url, regist_url, special_url):
    with sync_playwright() as p:
        # handle_fetch_request賦予值

        def handle_fetch_request(route, request):
            if "getDmmAccessToken" in request.url:
                print("Intercepted target request: getDmmAccessToken")

                def handle_response(response):
                    try:
                        if response.status == 200:
                            json_data = response.body()
                            response_json = json.loads(json_data.decode())
                            # 提取所需的 token、token_secret 和 userId
                            token = response_json.get('token')
                            token_secret = response_json.get('secret')
                            user_id = response_json.get('userId')
                            consumer_key = 0
                            consumer_secret = 0
                            app_version = 0

                            if token and token_secret and user_id:
                                print(f"Success: Token: {token}, Token Secret: {token_secret}, User ID: {user_id}")
                                print(f"第一次")
                                time.sleep(10)
                                main(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
                                print(f"第二次")
                                time.sleep(10)
                                main(consumer_key, consumer_secret, token, token_secret, user_id, app_version)
                                time.sleep(10)
                                browser.close()
                                
                            else:
                                print("Failed: Response data is incomplete.")
                        else:
                            print(f"Failed: Unexpected response status {response.status}")
                    except Exception as e:
                        print(f"Error while processing response: {e}")

                # 繼續請求並監聽回應
                route.continue_()
                page.on("response", handle_response)
            else:
                route.continue_()

        # 設定用戶資料存儲目錄
        user_data_dir = f"C:\\aaa\\{email}\\user_data_dir"
        os.makedirs(user_data_dir, exist_ok=True)
        

        # 使用一個標準的 User-Agent
        user_agent = generate_standard_user_agent()

        # 啟動瀏覽器上下文
        browser = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,  # 是否無頭模式
            viewport={"width": 1920, "height": 1080},  # 確保使用標準的解析度
            timezone_id="Asia/Tokyo",
            locale="ja-JP",
        )
        # 創建頁面
        page = browser.new_page()
        # 嘗試從已保存的瀏覽器狀態加載
        load_browser_context_state(browser, email)
        page.route("**/*", handle_fetch_request)
        print("綁定成功")
        #綁定成功
        註冊登入確認頁面(email, password, opengame_url, error_url, regist_url, special_url, browser, page)





def 註冊登入確認頁面(email, password, opengame_url, error_url, regist_url, special_url, browser, page):
    try:
            # 添加 cookies（跳過年齡確認）
        page.context.add_cookies([{
                "name": "age_check_done",
                "value": "1",
                "domain": ".dmm.com",
                "path": "/",
                "httpOnly": False,
                "secure": False
            }, {
                "name": "age_check_done",
                "value": "1",
                "domain": ".dmm.co.jp",
                "path": "/",
                "httpOnly": False,
                "secure": False
            }])
        skip_remaining_checks = False
        current_url = page.url
        if current_url == "https://play.games.dmm.co.jp/game/deeponer":
            print("Detected special URL, skipping further checks.")
            skip_remaining_checks = True
            # 打開登入頁面#確認第一次
        if not skip_remaining_checks:
            第一次(email, password, opengame_url, error_url, regist_url, browser, page)
        
        current_url = page.url
        if current_url == "https://play.games.dmm.co.jp/game/deeponer":
            print("Detected special URL, skipping further checks.")
            skip_remaining_checks = True
        if not skip_remaining_checks:
            第二次(email, password, opengame_url, error_url, regist_url, browser, page)
        current_url = page.url
        if current_url == "https://play.games.dmm.co.jp/game/deeponer":
            print("Detected special URL, skipping further checks.")
            skip_remaining_checks = True
            #確認第三次
        if not skip_remaining_checks:
            第三次(email, password, opengame_url, error_url, regist_url, browser, page)
        current_url = page.url
        if current_url == "https://play.games.dmm.co.jp/game/deeponer":
            print("Detected special URL, skipping further checks.")
            skip_remaining_checks = True
            #確認第四次
        if not skip_remaining_checks:
            第4次(email, password, opengame_url, error_url, regist_url, special_url, browser, page)
        save_browser_context_state(browser, email)
            # 等待頁面加載完成，並等待驗證碼的郵件
        time.sleep(10)
        time.sleep(600)
    except Exception as e:
        print(f"Error occurred for {email}: {e}")
        
    
        

    finally:
            # 確保關閉瀏覽器
        browser.close()






def 第4次(email, password, opengame_url, error_url, regist_url, special_url, browser, page):
    try:
        page.goto(opengame_url)
    except Exception as e:
        print(f"An error occurred: {e}")
    current_url = page.url
    if current_url == special_url:
        print(f"Skipping further checks, current URL is {special_url}")
    if error_url in current_url:
        start_game(page)

    elif opengame_url in current_url:
        enter_email(email, password, page)
    elif regist_url in current_url:
        選擇年齡(email, opengame_url, regist_url, browser, page)

def 第三次(email, password, opengame_url, error_url, regist_url, browser, page):

    time.sleep(4)
    current_url = page.url
    if error_url in current_url:
        start_game(page)

    elif opengame_url in current_url:
        enter_email(email, password, page)
    elif regist_url in current_url:
        選擇年齡(email, opengame_url, regist_url, browser, page)

def 第二次(email, password, opengame_url, error_url, regist_url, browser, page):
    current_url = page.url
    if error_url in current_url:
        start_game(page)

    elif opengame_url in current_url:
        enter_email(email, password, page)
    elif regist_url in current_url:
        選擇年齡(email, opengame_url, regist_url, browser, page)

def 第一次(email, password, opengame_url, error_url, regist_url, browser, page):
    try:
        page.goto(opengame_url)
    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(4)
    current_url = page.url
    
    if error_url in current_url:
        start_game(page)
    elif opengame_url in current_url:
        enter_email(email, password, page)
    elif regist_url in current_url:
        選擇年齡(email, opengame_url, regist_url, browser, page)
            #確認第二次
    time.sleep(10)

def 選擇年齡(email, opengame_url, regist_url, browser, page):
    print("目前在點選年齡頁面")
    time.sleep(10)
    try:
        save_browser_context_state(browser, email)
    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(1)
    try:
        select_date(page, year=1990, month=1, day=1)
    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(1)
    try:
        page.click('#commit_submit')
    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(20)
    browser.close()


def start_game(page):
    print("目前在點選開始遊戲頁面")
    try:
        page.click('a#game-play-top')
        
    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(10)

        



def enter_email(email, password, page):
    print("目前在點選登入FANZA頁面")
    try:
        page.fill('input[name="login_id"]', email)
    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(1)
    try:
        page.fill('input[name="password"]', password)
    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(1)
    try:
        page.check('input[name="use_auto_login"]')
    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(1)
    try:
        page.click('button[type="submit"]')
    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(30)
    page.context.add_cookies([{
        "name": "age_check_done",
        "value": "1",
        "domain": ".dmm.com",
        "path": "/",
        "httpOnly": False,
        "secure": False
    }, {
        "name": "age_check_done",
        "value": "1",
        "domain": ".dmm.co.jp",
        "path": "/",
        "httpOnly": False,
        "secure": False
    }])


def save_browser_context_state(context, email):
    """保存瀏覽器狀態（包括 cookies, localStorage, sessionStorage 等）"""
    state_dir = f"C:\\aaa\\{email}"
    os.makedirs(state_dir, exist_ok=True)
    state_path = os.path.join(state_dir, "browser_context_state.json")
    context.storage_state(path=state_path)  # 保存整個上下文狀態
    print(f"Browser context state for {email} saved to {state_path}")

def load_browser_context_state(context, email):
    """從已保存的狀態檔案中加載瀏覽器狀態"""
    state_dir = f"C:\\aaa\\{email}"
    state_path = os.path.join(state_dir, "browser_context_state.json")
    
    if os.path.exists(state_path):
        context.storage_state(path=state_path)  # 加載已保存的上下文狀態
        print(f"Browser context state for {email} loaded from {state_path}")
    else:
        print(f"No saved state for {email}, starting fresh.")




def select_date(page, year, month, day):
    # 選擇年份
    page.select_option('select#year', value=str(year))
    time.sleep(1)
    
    # 選擇月份
    page.select_option('select#month', value=f"{int(month):02d}")
    time.sleep(1)
    
    # 選擇日期
    page.select_option('select#day', value=f"{int(day):02d}")
    time.sleep(1)


