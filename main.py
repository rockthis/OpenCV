from selenium import webdriver
from time import sleep
import pyautogui


chop = webdriver.ChromeOptions()
chop.add_extension('/Users/kostyafrolov/Desktop/4.3.0_0.crx')

# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")


driver = webdriver.Chrome('/Users/kostyafrolov/Downloads/chromedriver',chrome_options=chop)

driver.get('http://google.com')

driver.set_window_size(1920, 1076)
driver.maximize_window()
page = driver.current_window_handle
driver.switch_to_window(page)

# screenWidth, screenHeight = pyautogui.size()
# currentMouseX, currentMouseY = pyautogui.position()
sleep(2)
pyautogui.moveTo(1876, 57)
pyautogui.click()
sleep(3)
im2 = pyautogui.screenshot(region=(1190,50,720, 650))
im2.save('img.png')
# print(driver.current_window_handle)
sleep(4)
driver.quit()

# 1190, 50
# 1910,702