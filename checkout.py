from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\\Documents\\chromwdriver.exe")
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element_by_path("//input[@id='user-name']").send_keys="standard_user"
driver.find_element_by_path("//input[@id='password']").send_keys="secret_sauce"
driver.find.element_by_path("//input[@id='login-button']").click()
time.sleep(5)

def checkout():
  if(driver.find_element_by_xpath("//*[@id="header_container"]/div[2]/span).is_displayed()):
    driver.find.element_by_path("//*[@id="checkout"]").click()
    if(driver.find.element_by_path("//*[@id="header_container"]/div[2]/span")):
      driver.find_element_by_path("//*[@id="first-name"]").send_keys="Shubham"
      driver.find_element_by_path("//*[@id="last-name"]").send_keys="Katare"
      driver.find_element_by_path("//*[@id="postal-code"]").send_keys="231001"
      driver.find.element_by_path("//*[@id="continue"]").click()
  else:
  print("Error in loading")

  
  
