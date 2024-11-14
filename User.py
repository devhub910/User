##i.vr7

import random
import time
from colorama import Fore, init

# تهيئة مكتبة colorama
init()

# قائمة الأكواد الوهمية الخاصة بمحاكاة اختراق حساب ديسكورد
fake_login_attempts = [
    "Attempting login to account: {user_account}",
    "Username: {user_account}",
    "Password: *********",
    "Login failed. Incorrect password.",
    "Attempting with different password...",
    "Access Denied! Retrying...",
    "Hacking into Discord account...",
    "Decrypting password hashes...",
    "Password found! *********",
    "Bypassing security checks...",
    "Accessing Discord settings...",
    "Changing email to hacked@example.com",
    "Account compromised! Unauthorized access.",
    "Bypassing 2FA...",
    "Access granted! Account now under control.",
    "Password: *********",
    "Login successful! Welcome {user_account}",
    "Downloading personal data...",
    "Uploading malware to account...",
    "Connecting to Discord server...",
    "Injecting malicious script...",
    "Exfiltrating data from Discord server...",
]

# وظيفة لطباعة النص ببطء لإضافة تأثير الرسوم المتحركة
def slow_print(text, color):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(0.02)  # تأخير طفيف بين الحروف
    print(Fore.RESET)

# دالة لطباعة الأكواد العشوائية بألوان الأحمر والأخضر مع الرسوم الكتابية
def fake_hacker_effect(user_account):
    colors = [Fore.RED, Fore.GREEN]  # الألوان المستخدمة
    fake_email = "saadvr7hamood@gmail.com"
    fake_password = "b5f62b0a35f4dfb25567d5a6b9405f3b"  # كلمة مرور مشفرة عشوائيًا

    # طباعة الرسالة الأولى
    slow_print(f"Welcome! Please enter the Discord account you want to hack:", Fore.GREEN)
    
    # طباعة عملية المحاكاة
    slow_print(f"Attempting to hack account with user '{user_account}'...", Fore.RED)
    slow_print("Access Denied! Please wait for 10 seconds...", Fore.RED)
    time.sleep(10)

    # طباعة تفاصيل الحساب المخترق
    slow_print("Email and password obtained:", Fore.GREEN)
    slow_print(f"UserAccount: {user_account}", Fore.GREEN)
    slow_print(f"GmailAccount: {fake_email}", Fore.GREEN)
    slow_print(f"PasswordAccount: {fake_password}", Fore.GREEN)

    # طباعة محاولات تسجيل الدخول
    slow_print(f"Attempting login to Discord account with the following details:", Fore.RED)
    time.sleep(2)  # تأخير بين المحاولات
    for attempt in range(5):
        slow_print(random.choice(fake_login_attempts).format(user_account=user_account), random.choice(colors))
        time.sleep(1)

# تشغيل الكود
if __name__ == "__main__":
    try:
        user_account = input("UserAccount: ")  # طلب اسم حساب ديسكورد من المستخدم
        fake_hacker_effect(user_account)
    except KeyboardInterrupt:
        print("\nتم إيقاف العرض")