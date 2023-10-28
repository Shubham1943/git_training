*** Settings ***

Library SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  xx-x-x--x\chromedriver.exe

*** Test Cases ***
LoginTest
    create webdriver    chrome  executable_path="xx-x-x--x\chromedriver.exe"
    Open browser    ${url}  ${browser}
    maximize browser window
    input text      id:user-name    standard_user
    input text      id:password     secret_sauce
    click element   xpath://input[@id='login-button']
    close browser
    
*** Keywords ***
loginToApplication
    create webdriver    chrome  executable_path="xx-x-x--x\chromedriver.exe"
    Open browser    ${url}  ${browser}
    maximize browser window
    ${username}     set variable    id:user-name   
    ${password}     set variable    id:password   
    
    element should be visible   ${username}  
    element should be visible   ${password}
    
    sleep   5
    
    input text      ${username}     standard_user
    input text      ${password}     secret_sauce
    click element   xpath://input[@id='login-button']
