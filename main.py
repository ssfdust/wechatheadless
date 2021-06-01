from selenium import webdriver
from pathlib import Path
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import os

url_prefix = os.environ.get("INJECTOR_URL_PREFIX", "https://127.0.0.1")

injectjs = f"""
var script = document.createElement('script')
script.src = '{url_prefix}/injector.js'
document.getElementsByTagName('head')[0].appendChild(script)
"""

options = Options()
options.headless = True

# profile_path = Path(__file__).parent / "ffprofile"
geckodriver_path = str(Path(__file__).parent / "bin/geckodriver")

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


def load(webdriver):
    webdriver.execute_script(injectjs)
    sleep(2)
    webdriver.execute_script("injector.run()")


def reload_(webdriver):
    webdriver.refresh()
    sleep(6)
    load(webdriver)


load(driver)


while True:
    sleep(180)
    print("刷新页面")
    reload_(driver)
