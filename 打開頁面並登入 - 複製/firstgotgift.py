import os
import json
from playwright.sync_api import sync_playwright
from fain.main import main
import time



def login_dmm_with_cookies(email, password):
    login_url = "https://accounts.dmm.co.jp/service/login/password/=/path=https%3A%2F%2Fpersonal.games.dmm.co.jp%2Fprofile%2Fregist%2Fskip%3Fback_url%3Dhttps%253A%252F%252Factivate.games.dmm.co.jp%252Fbrowser-game%252Finstall%252Fdeeponer/channel=games"

    with sync_playwright() as p:
        # 設定 user_data_dir
        user_data_dir = f"C:\\aaa\\{email}\\user_data_dir"
        os.makedirs(user_data_dir, exist_ok=True)

        # 啟動瀏覽器，並使用 user_data_dir
        browser = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,  # 使用資料夾來儲存用戶資料
            headless=True,  # 可設為 True 隱藏瀏覽器
            viewport={"width": 1920, "height": 1080},  # 設置瀏覽器大小
            timezone_id="Asia/Tokyo",  # 設置時區
            locale="ja-JP",  # 設置語言
        )
        
        # 創建頁面
        page = browser.new_page()
                    # 打開遊戲主頁
        

        # 嘗試從已保存的瀏覽器狀態加載
        load_browser_context_state(browser, email)


        # 設置抓取 fetch 請求的攔截
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
                                with open("登入第一次已成功.txt", "a") as file:
                                    file.write(email + "\n")
                                    print(f"Account {email} has been processed successfully.")
                                
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

        page.on('route', handle_fetch_request)
        print("Route handler registered successfully!")

        # 如果沒有狀態則進行登入
        
        if not os.path.exists(f"C:\\aaa\\{email}\\browser_context_state.json"):
            browser.add_cookies([{
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
            page.goto(login_url)
            page.route("**/getDmmAccessToken*", handle_fetch_request)
            

            # 設置 cookies，跳過年齡確認

            time.sleep(5)
            current_url = page.url
            if current_url != "https://play.games.dmm.co.jp/game/deeponer":

            # 輸入電子郵件和密碼
                page.fill('input[name="login_id"]', email)
                page.fill('input[name="password"]', password)
                time.sleep(5)

            # 勾選 "ログインしたままにする"（即“保持登入”）
                page.check('input[name="use_auto_login"]')
                time.sleep(5)

            # 點擊登入按鈕
                page.click('button[type="submit"]')
                time.sleep(5)
                browser.add_cookies([{
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
                page.goto(login_url)
                page.route("**/getDmmAccessToken*", handle_fetch_request)

            # 等待 5 秒鐘，防止過快跳轉
                page.wait_for_timeout(5000)

            # 等待頁面加載完成
                page.wait_for_load_state('load') 
            
            save_browser_context_state(browser, email)


            print(f"Logged in and navigated to: {page.url}")
            page.wait_for_timeout(500000)  # 這裡保證頁面保持開啟
            save_browser_context_state(browser, email)
        else:
            page.route("**/getDmmAccessToken*", handle_fetch_request)
            

            # 設置 cookies，跳過年齡確認
            browser.add_cookies([{
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
            page.goto(login_url)
            page.route("**/getDmmAccessToken*", handle_fetch_request)
            time.sleep(5)
            
            current_url = page.url
            if current_url != "https://play.games.dmm.co.jp/game/deeponer":
                browser.add_cookies([{
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
            page.goto(login_url)
            page.route("**/getDmmAccessToken*", handle_fetch_request)
        
            current_url = page.url
            if current_url != "https://play.games.dmm.co.jp/game/deeponer":
            # 輸入電子郵件和密碼
                page.fill('input[name="login_id"]', email)
                page.fill('input[name="password"]', password)
                time.sleep(5)

            # 勾選 "ログインしたままにする"（即“保持登入”）
                page.check('input[name="use_auto_login"]')
                time.sleep(5)

            # 點擊登入按鈕
                page.click('button[type="submit"]')
                time.sleep(5)

                browser.add_cookies([{
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
            

            # 等待 5 秒鐘，防止過快跳轉
            page.wait_for_timeout(5000)

            # 等待頁面加載完成
            page.wait_for_load_state('load') 
            save_browser_context_state(browser, email)
            print(f"Using saved state for {email}.")
            

            print(f"Navigated to: {page.url}")
            page.wait_for_timeout(500000)  # 保證頁面保持開啟

        try:
            # 保持瀏覽器開啟直到用戶手動關閉
            print("Press Enter to close the browser...")
            input()  # 等待用戶按 Enter 鍵後關閉瀏覽器
        finally:
            # 確保關閉瀏覽器
            browser.close()






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