# crawl fund data from 天天基金网
# home page：http://fund.eastmoney.com/
# author: ryjfgjl
# date: 2020-08-29

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
from crawl_fund import Fund
from crawl_jjjz import JJJZ

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

WAIT = WebDriverWait(driver, 5)

# 开放式基金
url = "http://fund.eastmoney.com/fund.html#os_0;isall_0;ft_;pt_1"
driver.get(url)

# crawl fund
Fund = Fund()
Fund.main(driver)
# crawl jjjz
JJJZ = JJJZ()
JJJZ.main(driver)











