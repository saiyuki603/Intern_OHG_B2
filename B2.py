import imp
from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver
import chromedriver_binary
import pandas as pd
import re
import os
import traceback
import C1
import mojimoji

def chiba_doro(address_list, err):
    """
    千葉の道路を取得する関数です。
    """
    try:

        err = 0

        list = address_list

        s1 = list[1]
        s2 = list[2]
        s3 = list[3]
        s4 = list[4]
        
        driver = webdriver.Chrome()
        
        actionChains = ActionChains(driver)
        
        # 処理時に最大10秒間待つ
        driver.implicitly_wait(10)
        driver.get("https://webgis.alandis.jp/chiba12/portal/index.html")
        
        # ページの下へスクロール
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        actionChains.click(driver.find_element(By.XPATH,"//*[@id='agree']")).perform()
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

        # 地図の中のエリアを探してクリックする
        driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/div/div/map/area[265]").click()
        time.sleep(3.5)
        actionChains.click(driver.find_element(By.XPATH,"//*[@id='sidemenu_tab_search']")).perform()
        time.sleep(1)

        actionChains.click(driver.find_element(By.XPATH,"//*[@id='sidemenu_menu_search_drilldown_1']/span")).perform()

        # ドロップダウンから入力内容を検索して、選択する
        d5 = driver.find_element(By.XPATH,"//*[@id='srh_search_drilldown_1_attrvalue_1']")
        select = Select(d5)
        select.select_by_visible_text(s1)

        d6 = driver.find_element(By.XPATH,"//*[@id='srh_search_drilldown_1_attrvalue_2']")
        select = Select(d6)
    # 丁目なし
        try:
            driver.implicitly_wait(1)
            select.select_by_visible_text(s2)

            d7 = driver.find_element(By.XPATH,"//*[@id='srh_search_drilldown_1_attrvalue_3']")
            select = Select(d7)
            # 全角から半角へ
            s3 = mojimoji.zen_to_han(s3)
            select.select_by_visible_text(s3)

    # 丁目あり
        except:
            driver.implicitly_wait(1)
            s3 = s3 + '丁目'
            s2 = s2 + s3 
            select.select_by_visible_text(s2)

            d7 = driver.find_element(By.XPATH,"//*[@id='srh_search_drilldown_1_attrvalue_3']")
            select = Select(d7)
            # 全角から半角へ
            s4 = mojimoji.zen_to_han(s4)

            select.select_by_visible_text(s4)
            actionChains.click(driver.find_element(By.XPATH,"//*[@id='srh_search_drilldown_1_btn']")).perform()

            # 余計なものを閉じる
            actionChains.click(driver.find_element(By.XPATH,"//*[@id='sidemenu_tab_search']")).perform()
            actionChains.click(driver.find_element(By.XPATH,"//*[@id='index_hidden']")).perform()
            time.sleep(1)
            
        # 相対パスにスクショをセーブする
        FILENAME1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B2.png')
        driver.save_screenshot(FILENAME1)

        driver.quit()

        return(err)

    # 下水だけとれる
    except:
        err = 3
        if err == 0:
            err = 3
            
    # 両方とも取れない
        elif err == 2:
            err = 1
            
        else:
            print("千葉県千葉市ではない") 
            err = 1
        return(err)

# B2(['千葉県千葉市','稲毛区','稲毛','３','７','３０'])