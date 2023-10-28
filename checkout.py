*** Settings ***

Library SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  xx-x-x--x\chromedriver.exe

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
    
    input text  name:firstName      demo
    input text  name:lastName       Kumar
    input text  name:postalCode     434343
    
    click element   xpath://*[@id="continue"]
    click element   xpath://*[@id="finish"]
    
    close browser
