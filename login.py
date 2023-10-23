from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\\Documents\\chromwdriver.exe")
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element_by_path("//input[@id='user-name']").send_keys="standard_user"
driver.find_element_by_path("//input[@id='password']").send_keys="secret_sauce"
driver.find.element_by_path("//input[@id='login-button']").click()

