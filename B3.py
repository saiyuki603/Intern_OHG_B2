import time

from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup
import time

import os

URL = 'http://www.geocoding.jp/api/'

def saitama_gesui(address_list):
    err = 0
    """
    addressに住所を指定すると緯度経度を返す。
    >>> coordinate('東京都文京区本郷7-3-1')
    ['35.712056', '139.762775']
    """

    address = "-".join(address_list)

    payload = {'q': address}
    xml = requests.get(URL, params=payload)
    soup = BeautifulSoup(xml.content, "xml")
    if soup.find('error'):
        err = 1
    latitude = soup.find('lat').string
    longitude = soup.find('lng').string

    soup = BeautifulSoup(xml.content, 'xml')
    found = soup.find('google_maps').string
    
    if found[-1] != '0' or found[-1] != '1' or found[-1] != '2' or found[-1] != '3' or found[-1] != '4' or found[-1] != '5' or found[-1] != '6' or found[-1] != '7' or found[-1] != '8' or found[-1] != '9':
        err = 1

    """
    埼玉の下水を検索・スクショ
    """
    gesui_url = 'https://www.sonicweb-asp.jp/saitama_g/map?theme=th_90#scale=500&pos=' + longitude + ',' + latitude
    driver = webdriver.Chrome()

    driver.get(gesui_url)
    time.sleep(5)

    iframe = driver.find_element(By.XPATH, '//*[@id="agreement_mask"]')
    driver.switch_to.frame(iframe)
    """
    iframe に移動
    """
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="agree_btn_area"]/ul/li[1]/a').click()
    driver.switch_to.default_content()
    """
    同意画面クリック
    """
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="footer"]/div[1]/a[18]').click()
    """
    縮尺変更
    """

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="side_menu_toggle_btn"]/div[1]').click()

    time.sleep(5)
    FILENAME = os.path.join(os.path.abspath(os.path.dirname(__file__)), "image\B3.png")

    driver.save_screenshot(FILENAME)
    return(err)