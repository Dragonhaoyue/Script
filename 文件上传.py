from selenium import webdriver
from time import sleep
import pyautogui     # pip install pyautogui -i https://mirrors.aliyun.com/pypi/simple


'''
文件上传的难点：弹出的是系统操作框，系统操作框无法定位元素
pyautoGui -- 自动操作 -- 控制鼠标、键盘执行操作
三大概念
1）、移动，move_to：坐标，把自己的坐标找到
2）、点击，click
3）、键盘输入
'''

driver = webdriver.Chrome()
driver.get('')
driver.maximize_window()

driver.find_element('id', 'name').click()
sleep(2)

# 移动到地址输入栏
pyautogui.moveTo(4323, 87)
sleep(2)
pyautogui.click()

# 清除原来的地址
pyautogui.press('backspace')
# 输入新的文件路径
pyautogui.write(r'文件地址')

sleep(2)

# 连续按下两次回车
pyautogui.press('enter')
pyautogui.press('enter')

# 选择文件
pyautogui.moveTo(4323, 2324)
sleep(2)
pyautogui.click()

# 连续按下两次回车
pyautogui.press('enter')
pyautogui.press('enter')
sleep(2)
