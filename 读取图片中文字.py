from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import cv2 as cv    # pip install opencv_python -i https://mirrors.aliyun.com/pypi/simple

# 这两个只需要安装: pip install pytesseract -i https://mirrors.aliyun.com/pypi/simple
import pytesseract
from PIL import Image


driver = webdriver.Chrome()

# 打开项目地址
driver.get('dizhi')

'''
验证码识别处理
1.加载图片（定位到元素，保存下来，imread）；2.降噪（颜色不深的东西抹除，pyrMeanShiftFiltering）
3.二值化（直接成黑白图片，threshold）；4.读文字（image_to_string）
'''

# 保存验证码图片到本地
driver.find_element(By.ID, 'chkd').screenshot('master_drawing.png')

sleep(3)    # 等待图片保存成功

# 读取原图
master_drawing = cv.imread('master_drawing.png')

# 对图片进行去噪处理
denoised_picture = cv.pyrMeanShiftFiltering(master_drawing, 10, 100)

# 对图片进行灰度处理
grayscale_picture = cv.cvtColor(denoised_picture, cv.COLOR_BGR2GRAY)

# 对图片进行二值化处理
threshold_value, binary_picture = cv.threshold(grayscale_picture, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imwrite('binary_picture.png', binary_picture)

# 使用PIL打开图像转化为图像对象，并使用pytesseract进行图像识别
binary_picture = 'binary_picture.png'
captcha_picture = Image.open(binary_picture)
verification_code = pytesseract.image_to_string(captcha_picture)
print('识别到的验证码为：', verification_code)

'''
验证码识别结束
'''