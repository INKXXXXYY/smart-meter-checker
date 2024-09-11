from PIL import Image
import pytesseract
import re

def capture_and_extract_balance(image_path, region):
    try:
        pyautogui.screenshot(image_path, region=region)
        image = Image.open(image_path)
        ocr_output = pytesseract.image_to_string(image)
        print("OCR 输出:", ocr_output)
        match = re.search(r"z\s*([0-9]+\.?[0-9]*)", ocr_output)
        if match:
            balance = float(match.group(1))
            print(f"提取到的余额: {balance}")
            return balance
        else:
            print("未能提取到余额数值")
            return None
    except Exception as e:
        print(f"提取电表余额失败: {e}")
        return None
