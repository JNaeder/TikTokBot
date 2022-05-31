import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


PATH = "C:/Users\jnaed\Downloads\chromedriver_win32\chromedriver.exe"
s = Service(PATH)

for i in range(5):
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.tiktok.com/login/phone-or-email/email")


# time.sleep(3)
# email_input = driver.find_element(By.CLASS_NAME, "e93gz7m1")
# print(email_input)
# email_input.send_keys("madhead324@gmail.com")
