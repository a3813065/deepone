from firstgotgift import login_dmm_with_cookies

# 根據範圍生成帳號和密碼列表
accounts = [{"email": f"SS{i}@SS", "password": "SS"} for i in range(150, 200)]

# 設置郵件伺服器地址
imap_server = "192.168.1.102"  # 替換為您郵箱的 IMAP 伺服器地址

if __name__ == "__main__":
    # 根據不同帳號執行註冊操作
    for account in accounts:
        email = account["email"]
        password = account["password"]
        try:
            print(f"Processing account: {email}")
            login_dmm_with_cookies(email, password)
        except Exception as e:
            print(f"Error logging in with {email}: {e}")
