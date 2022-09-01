import time

from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup
import time

import os

def saitama_doro(address_list):
    err = 0
    """
    addressに住所を指定すると緯度経度を返す。
    >>> coordinate('東京都文京区本郷7-3-1')
    ['35.712056', '139.762775']
    """
    URL = 'http://www.geocoding.jp/api/'

    address = "-".join(address_list)

    payload = {'q': address}
    xml = requests.get(URL, params=payload)
    soup = BeautifulSoup(xml.content, "xml")
    if soup.find('error'):
        err = 1
    latitude = soup.find('lat').string
    latitude = latitude.replace(',', '')
    longitude = soup.find('lng').string
    longitude = longitude.replace(',', '')

    soup = BeautifulSoup(xml.content, 'xml')
    found = soup.find('google_maps').string

    if found[-1] != '０' and found[-1] != '１' and found[-1] != '２' and found[-1] != '３' and found[-1] != '４' and found[-1] != '５' and found[-1] != '６' and found[-1] != '７' and found[-1] != '８' and found[-1] != '９':
        err = 1

    """
    埼玉の道路を検索・スクショ
    """
    doro_url = 'https://www.sonicweb-asp.jp/saitama_g/map?theme=th_31#scale=5000&pos=' + longitude + ',' + latitude
    driver = webdriver.Chrome()

    driver.get(doro_url)
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
    time.sleep(5)

    FILENAME = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B4.png')
    driver.save_screenshot(FILENAME)
    return(err)