*** Settings ***

Library SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  xx-x-x--x\chromedriver.exe
${F_NAME}   firstName
${L_NAME}   LastName

*** Test Cases ***
Checkout
    create webdriver    chrome  executable_path="xx-x-x--x\chromedriver.exe"
    Open browser    ${url}  ${browser}
    maximize browser window
    input text      id:user-name    standard_user
    input text      id:password     secret_sauce
    click element   xpath://input[@id='login-button']
    click element   xpath://a[@class='shopping_cart_link']
    
    title should be     'Your Cart'
    click element   xpath://*[@id="checkout"]
    
    sleep   5
    
    element should be visible   ${F_NAME}   
    element should be visible   ${L_NAME}
    

    IF      (${F_NAME} and ${L_NAME} != none)
        LOG     "Postal Code is required"
        
    ELIF    ${F_NAME} != none
        LOG     "Lastname is required"
        
    ELIF
        LOG     "Firstname is required"

    
    click element   xpath://*[@id="continue"]
    click element   xpath://*[@id="finish"]
    
    close browser
