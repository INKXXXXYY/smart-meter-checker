
# 智能电表余额查询

该项目是一个用于自动化检查智能电表余额的脚本，支持通过自定义操作步骤和图像路径进行操作，适配不同的公众号或应用程序。用户可以通过修改配置文件 `config.py` 自行配置不同的自动化流程。

本项目是以微信公众号查询，以朵拉国际公寓为例。
## 功能特色

- 自动化通过 GUI 检查智能电表的余额。
- 使用 OCR（Tesseract）提取余额信息。
- 如果余额低于阈值，发送电子邮件提醒。

## 安装步骤

1. 克隆项目仓库：
   ```bash
   git clone https://github.com/your_username/smart-meter-checker.git
   cd smart-meter-checker
   ```

2. 安装所需的依赖包：
   ```bash
   pip install -r requirements.txt
   ```

3. 在 `config.py` 中配置邮箱和相关路径。

## 使用方法

1. 运行主脚本：
   ```bash
   python main.py
   ```

## 自动化设置（Windows 任务计划程序）

你可以通过 Windows 任务计划程序（Task Scheduler）来定期运行此脚本，实现自动化执行：

1. 从开始菜单中打开任务计划程序。
2. 点击 **创建任务**，并为其命名。
3. 在 **触发器** 选项卡中，设置你希望脚本运行的时间（例如每天、每周等）。
4. 在 **操作** 选项卡中，点击 **新建**，选择 **启动程序**，然后浏览选择你的 Python 可执行文件路径（例如 `python.exe`）。
5. 在 **添加参数** 字段中，输入 `main.py` 文件的完整路径，例如：
   ```bash
   C:\path\to\main.py
   ```
6. 保存任务，任务计划程序将按照设定的时间自动运行你的脚本！

## 依赖项

- `pyautogui`
- `pytesseract`
- `Pillow`
- `smtplib`
- `psutil`

## 许可证

本项目基于 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

---

## 配置文件说明

在 `config.py` 中，你可以修改以下部分：

1. **APP_PATH**：这是你想自动化的应用程序路径，配置为你电脑中的快捷方式或可执行文件路径。
   ```python
   APP_PATH = r"C:\Users\你的路径\应用程序.lnk"
   ```

2. **BUTTONS**：按钮图像路径，用于定位按钮位置。请将对应步骤中的按钮截图并保存，然后更新路径：
   ```python
   BUTTONS = {
       "租约按钮": r"C:\你的路径\img.png",
       "智能设备": r"C:\你的路径\img_1.png",
       "智能电表": r"C:\你的路径\img_3.png",
       "关闭按钮": r"C:\你的路径\img_4.png"
   }
   ```

3. **STEPS**：步骤配置，根据实际操作流程的顺序，填写按钮名称和描述信息。该名称需要与 `BUTTONS` 中的键保持一致。
   ```python
   STEPS = [
       {"name": "租约按钮", "description": "点击租约按钮"},
       {"name": "智能设备", "description": "点击智能设备按钮"},
       {"name": "智能电表", "description": "点击智能电表按钮"},
       {"name": "关闭按钮", "description": "点击关闭按钮"}
   ]
   ```
4. **BALANCE_THRESHOLD**：设置电表余额的警告阈值。当电表余额低于此值时，系统会自动发送提醒邮件：
   ```python
   BALANCE_THRESHOLD = 30.0  # 默认值为30.0度，可以根据需求修改

5. **METER_SCREENSHOT_REGION**：配置截图区域，用于指定你要截图的屏幕区域。该区域是一个 `(left, top, width, height)` 的元组，分别表示截图的左上角位置和宽高。你需要根据电表余额在屏幕上的位置来调整这个区域。
   ```python
   METER_SCREENSHOT_REGION = (709, 50, 500, 1000)  # 根据实际显示位置修改

## 如何自定义流程

### 1. 更新应用程序路径
首先，找到你想要自动化的应用程序，并将其快捷方式或可执行文件的完整路径复制到 `APP_PATH` 中。

### 2. 创建截图
在应用程序中找到你需要点击的按钮，使用截图工具（例如 Windows 自带的截图工具）捕获按钮的图像并保存到某个目录下。然后将对应的图像路径更新到 `BUTTONS` 配置中。

### 3. 自定义步骤
根据实际的操作流程更新 `STEPS` 列表，确保步骤名称与 `BUTTONS` 中的键匹配。你可以添加或删除步骤，完全根据你的自动化流程需求自定义。

## 运行程序

完成配置后，运行主脚本来启动自动化任务：
```bash
python main.py
```
