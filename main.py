from automation import run_automation
from ocr_utils import capture_and_extract_balance
from email_utils import send_email
from config import METER_SCREENSHOT_PATH

def main():
    print("启动自动化任务...")

    # 运行自动化过程
    run_automation()

    # 提取电表余额
    balance = capture_and_extract_balance(METER_SCREENSHOT_PATH, (709, 50, 500, 1000))

    # 如果余额低于阈值，发送警告邮件
    if balance is not None and balance < 30:
        send_email("电表余额预警", f"警告：当前电表余额为 {balance} 度，请及时充值！")

    print("任务完成")

if __name__ == '__main__':
    main()
