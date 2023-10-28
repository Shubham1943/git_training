ibrary SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  xx-x-x--x\chromedriver.exe

*** Test Cases ***
add_to_cart
    create webdriver    chrome  executable_path="xx-x-x--x\chromedriver.exe"
    Open browser    ${url}  ${browser}
    maximize browser window
    input text      id:user-name    standard_user
    input text      id:password     secret_sauce
    click element   xpath://input[@id='login-button']
    
    click element   xpath://input[@id='remove-sauce-labs-backpack']
    click element   xpath://input[@id='remove-sauce-labs-bike-light']
    click element   xpath://input[@id='remove-sauce-labs-bolt-t-shirt']
    click element   xpath://input[@id='remove-sauce-labs-fleece-jacket']
    click element   xpath://input[@id='remove-sauce-labs-onesie']
    click element   xpath://input[@id='remove-test.allthethings()-t-shirt-(red)']
    
    click element   xpath://a[@class='shopping_cart_link']
    
    title should be     'Your Cart'
    
    click element   xpath://input[@id='//continue-shopping']
