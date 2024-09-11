import pyautogui
import time
import subprocess
from config import APP_PATH, BUTTONS, STEPS

def launch_application():
    try:
        subprocess.Popen([APP_PATH], shell=True)
        time.sleep(5)  # 等待应用程序启动
    except Exception as e:
        print(f"启动应用失败: {e}")

def click_button(image_path, description):
    button_location = pyautogui.locateOnScreen(image_path)
    if button_location:
        pyautogui.click(button_location)
        time.sleep(2)  # 确保点击后的UI响应
        print(f'{description} 点击成功')
        return True
    else:
        print(f'未找到 {description} 按钮')
        return False

def run_automation():
    # 启动应用程序
    launch_application()

    # 根据配置的步骤进行自动化操作
    for step in STEPS:
        image_path = BUTTONS.get(step["name"])
        if image_path:
            if not click_button(image_path, step["description"]):
                print(f"未找到 {step['description']}，可能操作失败")
                return
        else:
            print(f"未配置 {step['name']} 的图像路径")
