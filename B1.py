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
import mojimoji


def chiba(address_list):
  err = 0
  if '千葉市' in address_list[0]:
    
    try:
      list = address_list

      s1 = list[1]
      s2 = list[2]
      s3 = list[3]
      s4 = list[4]
      driver = webdriver.Chrome()
      driver.get("http://s-page.tumsy.com/chibagesui/index.html")
      time.sleep(2)

      # 同意する
      iframe = driver.find_element(By.XPATH,"/html/frameset/frame")
      driver.switch_to.frame(iframe)
      time.sleep(2)

      driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

      actionChains = ActionChains(driver)
      
      actionChains.click(driver.find_element(By.XPATH,"//*[@id='LinkButton1']")).perform()
      # driver.switch_to.default_content()
      time.sleep(5)
      
      d1 = driver.find_element(By.XPATH,"//*[@id='ELM_CMB_LEV1']")
      select = Select(d1)
      select.select_by_visible_text(s1)
      time.sleep(2)
      d2 = driver.find_element(By.XPATH,"//*[@id='ELM_CMB_LEV2']")
      select = Select(d2)
      select.select_by_visible_text(s2)
      time.sleep(2)

      d3 = driver.find_element(By.XPATH,"//*[@id='ELM_CMB_LEV3']")
      select = Select(d3)
      selected = select.all_selected_options

      if selected[0].text =="丁目なし":
        time.sleep(2)
        d4 = driver.find_element(By.XPATH,"//*[@id='ELM_CMB_LEV4']")
        select = Select(d4)
        s4 = s3 + "番地"
        select.select_by_visible_text(s4)
        time.sleep(2)
        a = 0
      else:
        d3 = driver.find_element(By.XPATH,"//*[@id='ELM_CMB_LEV3']")
        select = Select(d3)
        s3 = s3 + "丁目"
        select.select_by_visible_text(s3)
        time.sleep(2)
        d4 = driver.find_element(By.XPATH,"//*[@id='ELM_CMB_LEV4']")
        select = Select(d4)
        s4 = s4 + "番"
        select.select_by_visible_text(s4)
        time.sleep(2)
        a = 1

      actionChains.click(driver.find_element(By.XPATH,"//*[@id='btnAddSchDlgOK']")).perform()
      time.sleep(2)
      FILENAME = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B-1.png')
      driver.save_screenshot(FILENAME)

      driver.get("https://webgis.alandis.jp/chiba12/portal/index.html")
      time.sleep(2)

      driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
      actionChains.click(driver.find_element(By.XPATH,"//*[@id='agree']")).perform()
      time.sleep(2)
      
      driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
      driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/div/div/map/area[265]").click()
      time.sleep(4)
      actionChains.click(driver.find_element(By.XPATH,"//*[@id='sidemenu_tab_search']")).perform()
      time.sleep(2)
      
      actionChains.click(driver.find_element(By.XPATH,"//*[@id='sidemenu_menu_search_drilldown_1']/span")).perform()
      time.sleep(2)

      d5 = driver.find_element(By.XPATH,"//*[@id='srh_search_drilldown_1_attrvalue_1']")
      select = Select(d5)
      select.select_by_visible_text(s1)
      time.sleep(5)
      
      d6 = driver.find_element(By.XPATH,"//*[@id='srh_search_drilldown_1_attrvalue_2']")
      select = Select(d6)
      # 丁目なし
      if a == 0:
        select.select_by_visible_text(s2)
        time.sleep(5)
        d7 = driver.find_element(By.XPATH,"//*[@id='srh_search_drilldown_1_attrvalue_3']")
        select = Select(d7)
        s3 = mojimoji.zen_to_han(s3)
        select.select_by_visible_text(s3)
        
      # 丁目あり
      else:
        s2 = s2 + s3 
        select.select_by_visible_text(s2)
        time.sleep(5)
        d7 = driver.find_element(By.XPATH,"//*[@id='srh_search_drilldown_1_attrvalue_3']")
        select = Select(d7)
        s4 = s4[:-1]
        s4 = mojimoji.zen_to_han(s4)

        select.select_by_visible_text(s4)

      time.sleep(2)
      actionChains.click(driver.find_element(By.XPATH,"//*[@id='srh_search_drilldown_1_btn']")).perform()
      time.sleep(5)
      actionChains.click(driver.find_element(By.XPATH,"//*[@id='sidemenu_tab_search']")).perform()
      time.sleep(2)
      actionChains.click(driver.find_element(By.XPATH,"//*[@id='index_hidden']")).perform()
      time.sleep(2)
      
      FILENAME1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B-2.png')
      driver.save_screenshot(FILENAME1)

      driver.quit()
    
    except:
      err = 1

  else:
    print("千葉県千葉市ではない") 
    err = 1
  return(err)