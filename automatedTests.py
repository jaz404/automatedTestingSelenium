# Resolver Automation Challenge
# Code written by Jaspreet Singh Chhabra
# Date: 28th March 2024

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
# Creating instance of Chrome Webdriver
driver = webdriver.Chrome()
# Opening the given page

# Test 1

driver.get(r"file://C:\Users\jaspr\OneDrive\Desktop\AutomationChallenge-2024\index.html")                               # Navigating to home page


elementEmail = driver.find_element(By.ID, "inputEmail")                                                                 # Finding if email input is present
elementPassword = driver.find_element(By.ID, "inputPassword")                                                           # Finding if password input is present
elementLoginButton = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-block[type='submit']")     # Finding if login button is there
assert elementEmail is not None
elementEmail.send_keys("username@ualberta.ca")
assert elementPassword is not None
elementPassword.send_keys("password123")
assert elementLoginButton is not None


# Test 2

elementList = driver.find_element(By.CLASS_NAME, "list-group")

elementListItems = elementList.find_elements(By.TAG_NAME, "li")
assert len(elementListItems)==3, "There are not three values in the listgroup"
#print(elementListItems[1].text.strip())
elementList = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/ul/li[2]")
print(elementList.text[:-2])
assert elementList.text[:-2].strip() == "List Item 2", "The second item's value is not set to 'List Item 2'"

elementList = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/ul/li[2]/span")

assert elementList.text.strip() == "6", "The second item's value is not set to 'List Item 2'"

# Test 3
#wait = WebDriverWait(driver, 10)

#test_3_div = wait.until(EC.visibility_of_element_located((By.ID, "test-3-div")))

dropdowndiv = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div/button")
print(dropdowndiv.text)
assert dropdowndiv.text.strip() == "Option 1"

dropdowndiv.click()

option1btn = driver.find_element(By.XPATH,"/html/body/div/div[3]/div/div/div/a[3]")
option1btn.click()
#time.sleep(3)

# Test 4
btn1 = driver.find_element(By.XPATH,"/html/body/div/div[4]/div/button[1]")
btn2 = driver.find_element(By.XPATH,"/html/body/div/div[4]/div/button[2]")

assert btn1.is_enabled(), "btn 1 is not enabled"
assert not btn2.is_enabled(), "btn 2 is not disabled"



# Test 5
wait = WebDriverWait(driver, 10)
test_5_div = wait.until(EC.visibility_of_element_located((By.ID, "test-5-div")))

if test_5_div:
    btnDisplayed = False
    #while not btnDisplayed:
   #     try:
            #buttonDisp = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='button']")))
            #button_div5 = test_5_div.find_element(By.XPATH, "//button[@type='button']")
    #        btnDisplayed = True
      #  except:
      #      time.sleep(1)
    
    # Wait for the button to be displayed
    #buttonDisp = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='button']")))
    #print(buttonDisp)
    #buttonDisp.click()
    # revealed = test_5_div.find_element(By.ID, "test5-button")
    # wait = WebDriverWait(driver, timeout=10)
    # wait.until(lambda d : revealed.is_displayed())
    
    wait = WebDriverWait(driver, 20)
    button = wait.until(EC.element_to_be_clickable((By.ID, "test5-button")))
    
    button.click()
    sucessMsgLocation = (By.XPATH,"//div[@id='test5-alert']" )
    sucessMsg = wait.until(EC.visibility_of_element_located(sucessMsgLocation))
    assert sucessMsg.is_displayed(), "Success message is not displayed."
    
    #print("btn click")
    #button_div5.click()
    # Wait for success message
   
    #assert sucessMsg.is_displayed()
    #time.sleep(3)
    
    # time.sleep(7) 
    # button = test_5_div.find_element(By.XPATH, "//button[@type='button']")
    # button.click()
    
    







driver.quit()
