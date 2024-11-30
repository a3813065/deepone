from firstlogin import opengame

# 帳號和密碼列表
accounts = [
    {"email": "SS@SS", "password": "SS"},
    {"email": "SS@SS", "password": "SS"},
    # 可以在這裡繼續添加更多帳號
]

# 設置郵件伺服器地址
imap_server = "192.168.1.102"  # 替換為您郵箱的 IMAP 伺服器地址

if __name__ == "__main__":
    # 根據不同帳號執行註冊操作
    for account in accounts:
        email = account["email"]
        password = account["password"]
        try:
            print(f"Processing account: {email}")
            opengame(email, password, imap_server)
        except Exception as e:
            print(f"Error logging in with {email}: {e}")