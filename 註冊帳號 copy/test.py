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
        # 確保 Chrome 已啟動並啟用遠端調試，使用 http://localhost:9222
        cdp_url = "http://127.0.0.1:9222"
        browser = p.chromium.connect_over_cdp(cdp_url)
        
        # 使用第一個瀏覽器上下文
        context = browser.contexts[0]
        
        try:
            # 創建新頁面
            page = context.new_page()

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
            time.sleep(2)

            # 填寫表單
            page.fill('input[name="email"]', email)
            time.sleep(1)
            page.fill('input[name="password"]', password)
            time.sleep(1)

            # 點擊登入按鈕
            page.click('button[type="submit"]')

            # 等待頁面加載並處理驗證碼
            page.wait_for_load_state('networkidle')  # 等待頁面完全加載完成
            time.sleep(5)

            # 從郵箱中獲取驗證碼
            verification_code = get_verification_code(email, imap_server)
            time.sleep(5)

            驗證碼模塊(email, page, verification_code)

            time.sleep(10)

        except Exception as e:
            print(f"Error occurred for {email}: {e}")
            time.sleep(20)

        finally:
            # 確保關閉瀏覽器連接
            time.sleep(20)
            browser.close()

def 驗證碼模塊(email, page, verification_code, max_retries=3):
    """驗證碼填寫模塊，並處理頁面重載情況"""
    retries = 0
    
    while retries < max_retries:
        try:
            if verification_code:
                print(f"Verification code received: {verification_code}")

                # 取得所有的輸入框
                input_fields = page.query_selector_all('input.css-v983ym')
                print(f"Found {len(input_fields)} input fields: {input_fields}")

                if len(input_fields) == 6:  # 確保有6個輸入框
                    for i, digit in enumerate(verification_code):
                        input_fields[i].fill(digit)  # 填寫對應的數字
                        print(f"Entering digit {i + 1}: {digit}")  # 顯示目前輸入第幾個和數字
                        
                        # 在每次填寫後確保頁面穩定並等待
                        time.sleep(1)  # 等待1秒確保填寫完成
                        if i == 5:  # 如果是最後一個輸入框，等待頁面加載
                            time.sleep(2)  # 等待加載完成

                    # 確保清理 cookies
                    page.context.clear_cookies()

                    # 註冊成功後將 email 寫入 999.txt 檔案
                    with open("註冊表.txt", "a") as file:
                        file.write(email + "\n")
                    print(f"Account {email} has been processed successfully.")
                    return  # 成功後返回
                else:
                    print("Couldn't find all 6 verification code input fields.")
                    time.sleep(2)

            else:
                print("Failed to retrieve verification code.")
                time.sleep(2)
        
        except Exception as e:
            print(f"Error occurred for {email}: {e}")
            if "Execution context was destroyed" in str(e):
                # 如果發生頁面加載或導航錯誤，重新嘗試
                retries += 1
                print(f"Retrying ({retries}/{max_retries})...")

                # 重新加載頁面並等待頁面穩定
                page.reload()
                time.sleep(5)  # 等待頁面加載完成
            else:
                break  # 如果是其他錯誤，則退出

    print(f"Failed to process account {email} after {max_retries} retries.")