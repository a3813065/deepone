import os
import random
from playwright.sync_api import sync_playwright
from mail import get_verification_code  # 引入 mail.py 的函數
import time

def generate_standard_user_agent():
    """生成一個常見且有效的 User-Agent 字串，並包含 Edge 瀏覽器"""
    
    return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62"

def register_dmm(email, password, imap_server):
    """用於自動化註冊 DMM 帳戶的函數"""
    login_url = "https://accounts.dmm.co.jp/welcome/signup/email/=/back_url=https%3A%2F%2Fgames.dmm.co.jp%2F/channel=games?auth_method_type=email"

    with sync_playwright() as p:
        # 設定用戶資料存儲目錄
        user_data_dir = f"C:\\aaa\\{email}\\user_data_dir"
        os.makedirs(user_data_dir, exist_ok=True)

        # 使用一個標準的 User-Agent
        user_agent = generate_standard_user_agent()

        # 啟動瀏覽器上下文
        browser = p.chromium.launch_persistent_context(
        user_data_dir=user_data_dir,  # 設定用戶資料目錄
        executable_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",  # 指定本地 Edge 執行檔的路徑
        args=["--start-maximized", "--disable-blink-features=AutomationControlled"],  # 禁用自動化檢測特徵
        headless=False,  # 是否顯示瀏覽器界面
        viewport={"width": 1920, "height": 1080},  # 設定解析度
        timezone_id="Asia/Tokyo",  # 設定時區
        locale="ja-JP",  # 設定語言區域
        user_agent=user_agent  # 使用標準的 User-Agent
    )

        try:
            # 創建頁面
            page = browser.new_page()
            

            # 添加 cookies（跳過年齡確認）
            page.context.add_cookies([{
                "name": "age_check_done",
                "value": "1",
                "domain": ".dmm.com",
                "path": "/",
                "httpOnly": False,
                "secure": False
            }])

            # 打開登入頁面
            page.goto(login_url)
            time.sleep(5)

            # 填寫表單
            
            page.fill('input[name="email"]', email)
            time.sleep(5)
            page.fill('input[name="password"]', password)
            time.sleep(5)

            # 點擊登入按鈕
            page.click('button[type="submit"]')

            # 等待頁面加載完成，並等待驗證碼的郵件
            time.sleep(15)

            # 從郵箱中獲取驗證碼
            verification_code = get_verification_code(email, imap_server)

            if verification_code:
                print(f"Verification code received: {verification_code}")

                # 分別填寫每個輸入框
                input_fields = page.query_selector_all('input.css-1nd5pp0')  # 這裡選擇所有帶有特定 class 的 input
                if len(input_fields) == 6:  # 確保有6個輸入框
                    for i, digit in enumerate(verification_code):
                        input_fields[i].fill(digit)  # 填寫對應的數字
                        print(f"Entering digit {i + 1}: {digit}")  # 顯示目前輸入第幾個和數字

                    # 點擊確認
                    # 等待頁面加載完成
                    time.sleep(5)

                    # 註冊成功後將 email 寫入 999.txt 檔案
                    with open("999.txt", "a") as file:
                        file.write(email + "\n")

                    browser.close()

                    print(f"Account {email} has been processed successfully.")
                else:
                    print("Couldn't find all 6 verification code input fields.")

            else:
                print("Failed to retrieve verification code.")

        except Exception as e:
            print(f"Error occurred for {email}: {e}")

        finally:
            # 確保關閉瀏覽器
            browser.close()
