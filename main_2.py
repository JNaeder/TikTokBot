import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

PATH = "C:/Users/jnaed/Downloads/chromedriver_win32/chromedriver.exe"
s = Service(PATH)

for i in range(5):
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.tiktok.com/login/phone-or-email/email")
    driver.maximize_window()
    pyautogui.moveTo(952, 327)
    pyautogui.click()
    pyautogui.write("madhead324@gmail.com")
    pyautogui.press('tab')
    pyautogui.write("rhHiK32&ES5@VZmm!$@r")
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')


# while True:
#     print(pyautogui.position())

# screen_width, screen_height = pyautogui.size()
# print(pyautogui.position())
# pyautogui.moveTo(952, 331)
# pyautogui.click()
# pyautogui.write("madhead324@gmail.com")
# pyautogui.press('tab')
# pyautogui.write("rhHiK32&ES5@VZmm!$@r")
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.press('enter')

