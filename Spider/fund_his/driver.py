# chrome driver

import re, os
import json
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


class Driver:

    def main(self):
        binary_location = '/usr/bin/google-chrome'
        chrome_driver_binary = '/usr/bin/chromedriver'

        chrome_options = Options()
        chrome_options.binary_location = binary_location
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')

        chromedriver = chrome_driver_binary
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)
        return driver

