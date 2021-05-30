from selenium import webdriver
from pathlib import Path
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import os

injectjs = """
var script = document.createElement('script')
script.src = 'https://127.0.0.1:9000/injector.js'
document.getElementsByTagName('head')[0].appendChild(script)
"""

options = Options()
options.headless = True

# profile_path = Path(__file__).parent / "ffprofile"
geckodriver_path = str(Path(__file__).parent / "bin/geckodriver")

# profile = FirefoxProfile(profile_path)

# driver = webdriver.Firefox(options=options, firefox_profile=profile_path, executable_path=geckodriver_path)
driver = webdriver.Firefox(options=options, executable_path=geckodriver_path)
driver.get("https://wx.qq.com")
sleep(8)
element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/img")
element.screenshot("./qrcode.png")
print("生成qrcode.png")
while True:
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[1]/img")
        os.remove("./qrcode.png")
        print("删除qrcode.png")
        break
    except NoSuchElementException:
        print("not login")
        sleep(2)
driver.execute_script(injectjs)
sleep(2)
driver.execute_script("injector.run()")
