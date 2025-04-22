from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com") # getting the google page

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")) 
    ) # pauses web automation for 20 seconds until it finds the class name "gLFyf"

input = driver.find_element(By.CLASS_NAME, "gLFyf") #get to google's textbox field
input.clear() # Clear textbox field
input.send_keys("https://www.espn.com/nfl/team/_/name/bal/baltimore-ravens" + Keys.ENTER) # going to ESPN.com

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "ESPN")) 
    ) # pauses web automation for 20 seconds until is finds a link with ESPN

link = driver.find_element(By.PARTIAL_LINK_TEXT, "ESPN") # looking for the first link with ESPN
link.click()

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Roster")) 
    ) # pauses web automation for 30 seconds until it finds a string "Roster"

roster = driver.find_element(By.LINK_TEXT, "Roster")
roster.click()

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Lamar Jackson")) 
    ) # pauses web automation for 30 seconds until is finds a string "Lamar Jackson"

mvp = driver.find_element(By.LINK_TEXT, "Lamar Jackson")
mvp.click()

time.sleep(500)
driver.quit()