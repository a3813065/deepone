from test import register_dmm
import time
# 動態生成帳號和密碼列表，從 aaaaa10 到 aaaaa100
accounts = [{"email": f"SS{i}@SS", "password": "SS"} for i in range(212, 300)]

# 設置郵件伺服器地址

imap_server = "192.168.1.102"  # 替換為您郵箱的 IMAP 伺服器地址

if __name__ == "__main__":
    # 根據不同帳號執行註冊操作
    for account in accounts:
        email = account["email"]
        password = account["password"]
        try:
            print(f"Processing account: {email}")
            register_dmm(email, password, imap_server)
            time.sleep(10)
        except Exception as e:
            print(f"Error logging in with {email}: {e}")
            time.sleep(10)
