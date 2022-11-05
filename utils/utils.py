import os

from selenium import webdriver

from pathlib import Path
DIR_HOME = str(Path.home())

import warnings
warnings.filterwarnings('ignore')


def create_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(os.path.join(DIR_HOME, "projects", "chromedriver"), chrome_options=chrome_options)
    return driver