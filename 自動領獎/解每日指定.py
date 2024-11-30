from login_dmm_with_cookies import login_dmm_with_cookies

# 帳號和密碼列表
accounts = [
    {"email": "SS@SS", "password": "SS"},
    {"email": "SS@ss", "password": "SS"},
    # 可以在這裡繼續添加更多帳號
]

if __name__ == "__main__":
    # 根據不同帳號執行登入操作
    for account in accounts:
        email = account["email"]
        password = account["password"]
        try:
            login_dmm_with_cookies(email, password)
        except Exception as e:
            print(f"Error logging in with {email}: {e}")
