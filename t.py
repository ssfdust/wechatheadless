from selenium import webdriver
from pathlib import Path
from selenium.webdriver.firefox.options import Options
from time import sleep

options = Options()
options.headless = False

geckodriver_path = str(Path(__file__).parent / "bin/geckodriver")
