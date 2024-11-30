import imaplib
import email
import re
import socket
import time
def get_verification_code(email_address, imap_server, imap_port=993):
    """從郵件伺服器提取驗證碼（使用加密連接）"""
    try:
        # 固定密碼
        email_password = "SS"
        time.sleep(10)
        # 連接到 IMAP 伺服器，使用 SSL 加密
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        
        # 登錄到郵件帳號
        mail.login(email_address, email_password)  # 登錄

        mail.select("inbox")  # 選擇收件箱

        # 搜索最近未讀的郵件
        status, messages = mail.search(None, 'UNSEEN')  # 搜索所有未讀郵件
        if status != "OK" or not messages[0]:
            print("No new messages found.")
            return None
        message_numbers = messages[0].split()[::-1]  # 反轉消息列表

        # 處理郵件
        for num in message_numbers[0].split():
            status, msg_data = mail.fetch(num, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])  # 解析郵件
                    subject = msg["subject"]  # 郵件主題
                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain":
                                body = part.get_payload(decode=True).decode()
                                break
                    else:
                        body = msg.get_payload(decode=True).decode()

                    # 在郵件正文中提取驗證碼（假設為 4 到 6 位數字）
                    match = re.search(r'\b\d{4,6}\b', body)
                    if match:
                        print(f"Verification code found: {match.group()}")
                        return match.group()

        print("Verification code not found.")
        return None

    except socket.error as e:
        print(f"Network error: {e}")
        return None
    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {e}")
        return None
    except Exception as e:
        print(f"Error accessing mail: {e}")
        return None

    finally:
        try:
            mail.logout()
        except imaplib.IMAP4.error as e:
            print(f"Error logging out: {e}")
