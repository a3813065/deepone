import os
from login_dmm_with_cookies import login_dmm_with_cookies

# 根據範圍生成帳號和密碼列表
accounts = [{"email": f"SS{i}@SS", "password": "SS"} for i in range(121, 200)]

# 設置文件名
completed_file = "每日登入完成表.txt"

def load_completed_accounts(file_path):
    """讀取已完成的帳號列表"""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            # 去除空行和多餘空白
            return set(line.strip() for line in file if line.strip())
    return set()

def main():
    # 讀取已完成的帳號
    completed_accounts = load_completed_accounts(completed_file)
    print(f"已完成的帳號: {completed_accounts}")

    # 過濾出未完成的帳號
    pending_accounts = [acc for acc in accounts if acc["email"] not in completed_accounts]

    for account in pending_accounts:
        email = account["email"]
        password = account["password"]
        try:
            print(f"Processing account: {email}")
            # 呼叫你的功能
            login_dmm_with_cookies(email, password)
            print(f"Success: {email}")
        except Exception as e:
            print(f"Error logging in with {email}: {e}")

if __name__ == "__main__":
    main()
