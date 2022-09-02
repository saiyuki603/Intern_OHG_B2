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


def chiba_gesui(address_list):
  err = 0
  if '千葉市' in address_list[0]:
    
    try:
      list = address_list

      s1 = list[1]
      s2 = list[2]
      s3 = list[3]
      s4 = list[4]
      driver = webdriver.Chrome()

      driver.implicitly_wait(10)

      driver.get("http://s-page.tumsy.com/chibagesui/index.html")

      # 同意する
      iframe = driver.find_element(By.XPATH,"/html/frameset/frame")
      driver.switch_to.frame(iframe)

      driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

      actionChains = ActionChains(driver)
      
      actionChains.click(driver.find_element(By.XPATH,"//*[@id='LinkButton1']")).perform()
      
      d1 = driver.find_element(By.XPATH,"//*[@id='ELM_CMB_LEV1']")
      select = Select(d1)
      select.select_by_visible_text(s1)

      d2 = driver.find_element(By.XPATH,"//*[@id='ELM_CMB_LEV2']")
      select = Select(d2)
      select.select_by_visible_text(s2)


      d3 = driver.find_element(By.XPATH,"//*[@id='ELM_CMB_LEV3']")
      select = Select(d3)
      selected = select.all_selected_options

      if selected[0].text =="丁目なし":
        d4 = driver.find_element(By.XPATH,"//*[@id='ELM_CMB_LEV4']")
        select = Select(d4)
        s4 = s3 + "番地"
        select.select_by_visible_text(s4)
        a = 0
      else:
        d3 = driver.find_element(By.XPATH,"//*[@id='ELM_CMB_LEV3']")
        select = Select(d3)
        s3 = s3 + "丁目"
        select.select_by_visible_text(s3)
        d4 = driver.find_element(By.XPATH,"//*[@id='ELM_CMB_LEV4']")
        select = Select(d4)
        s4 = s4 + "番"
        select.select_by_visible_text(s4)
        a = 1

      actionChains.click(driver.find_element(By.XPATH,"//*[@id='btnAddSchDlgOK']")).perform()
      time.sleep(3)
      FILENAME = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B1.png')
      driver.save_screenshot(FILENAME)
      # 道路だけとれる
    except:
      err = 2
    

  return(err, a)

# chiba(['千葉県千葉市','稲毛区','稲毛','３','７','３０'])