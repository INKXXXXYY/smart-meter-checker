# 邮件配置
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 465
SENDER_EMAIL = "example@qq.com"
RECEIVER_EMAIL = "example@qq.com"
PASSWORD = "your_email_password"

# 截图保存路径
METER_SCREENSHOT_PATH = r''

# Tesseract-OCR 路径
TESSERACT_PATH = r''

# config.py

# 应用程序路径
APP_PATH = r""

# 按钮图像路径配置
BUTTONS = {
    "租约按钮": r"",
    "智能设备": r"",
    "智能电表": r"",
    "关闭按钮": r""
}

# 步骤配置：可根据不同的操作流程自定义顺序
STEPS = [
    {"name": "租约按钮", "description": "点击租约按钮"},
    {"name": "智能设备", "description": "点击智能设备按钮"},
    {"name": "智能电表", "description": "点击智能电表按钮"},
    {"name": "关闭按钮", "description": "点击关闭按钮"}
]
