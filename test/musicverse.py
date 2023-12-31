# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
# driver = webdriver.Chrome(options = chrome_options)

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(options = chrome_options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_login(self):
    # Test name: login
    # Step # | name | target | value | comment
    # 1 | open | / |  | 
    self.driver.get("https://musicverse.onrender.com/")
    # 2 | setWindowSize | 1680x1019 |  | 
    self.driver.set_window_size(1680, 1019)
    # 3 | click | linkText=Login |  | 
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    # 4 | mouseOver | linkText=Login |  | 
    element = self.driver.find_element(By.LINK_TEXT, "Login")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 5 | mouseOut | linkText=Login |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 6 | click | css=.mb-4:nth-child(2) > .shadow |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .shadow").click()
    # 7 | type | css=.mb-4:nth-child(2) > .shadow | sean | 
    self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .shadow").send_keys("sean")
    # 8 | type | css=.mb-4:nth-child(4) > .shadow | password | 
    self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(4) > .shadow").send_keys("password")
    # 9 | sendKeys | css=.mb-4:nth-child(4) > .shadow | ${KEY_ENTER} | 
    self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(4) > .shadow").send_keys(Keys.ENTER)
    # 10 | click | linkText=Users |  | 
    self.driver.find_element(By.LINK_TEXT, "Users").click()
    # 11 | click | linkText=sean |  | 
    self.driver.find_element(By.LINK_TEXT, "sean").click()
    # 12 | click | linkText=Edit |  | 
    self.driver.find_element(By.LINK_TEXT, "Edit").click()
    # 13 | click | linkText=Scores |  | 
    self.driver.find_element(By.LINK_TEXT, "Scores").click()
    # 14 | click | linkText=sometitle |  | 
    self.driver.find_element(By.LINK_TEXT, "sometitle").click()
    # 15 | click | css=.px-6 |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".px-6").click()
    # 16 | click | css=.gpa-1 > div:nth-child(3) |  | 
    self.vars["window_handles"] = self.driver.window_handles
    # 17 | storeWindowHandle | root |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".gpa-1 > div:nth-child(3)").click()
    # 18 | selectWindow | handle=${win9063} |  | 
    self.vars["win9063"] = self.wait_for_window(2000)
    # 19 | close |  |  | 
    self.vars["root"] = self.driver.current_window_handle
    # 20 | selectWindow | handle=${root} |  | 
    self.driver.switch_to.window(self.vars["win9063"])
    # 21 | click | linkText=Upload |  | 
    self.driver.close()
    # 22 | click | id=title |  | 
    self.driver.switch_to.window(self.vars["root"])
    # 23 | type | id=title | somepdf | 
    self.driver.find_element(By.LINK_TEXT, "Upload").click()
    # 24 | type | id=author | somebody | 
    self.driver.find_element(By.ID, "title").click()
    # 25 | type | id=genre | somegenre | 
    self.driver.find_element(By.ID, "title").send_keys("somepdf")
    # 26 | type | id=price | 444 | 
    self.driver.find_element(By.ID, "author").send_keys("somebody")
    # 27 | click | css=.border-gray-400:nth-child(1) |  | 
    self.driver.find_element(By.ID, "genre").send_keys("somegenre")
    # 28 | type | css=.border-gray-400:nth-child(1) | C:\fakepath\Relations Mastery Workbook (with proof) (1).pdf | 
    self.driver.find_element(By.ID, "price").send_keys("444")
    # 29 | click | css=.hover\3A bg-green-600 |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".border-gray-400:nth-child(1)").click()
    # 30 | assertAlert | Score uploaded successfully! |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".border-gray-400:nth-child(1)").send_keys("C:\\fakepath\\Relations Mastery Workbook (with proof) (1).pdf")
    # 31 | click | linkText=Scores |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".hover\\3A bg-green-600").click()
    # 32 | click | linkText=somepdf |  | 
    assert self.driver.switch_to.alert.text == "Score uploaded successfully!"
    # 33 | runScript | window.scrollTo(0,0) |  | 
    self.driver.find_element(By.LINK_TEXT, "Scores").click()
    # 34 | click | css=.gpa-1 > div:nth-child(3) |  | 
    self.driver.find_element(By.LINK_TEXT, "somepdf").click()
    # 35 | selectWindow | handle=${win3531} |  | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 36 | close |  |  | 
    self.vars["window_handles"] = self.driver.window_handles
    # 37 | selectWindow | handle=${root} |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".gpa-1 > div:nth-child(3)").click()
    self.vars["win3531"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win3531"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
  
