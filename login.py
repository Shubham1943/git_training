
*** Settings ***

Library SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}      xx-x-x--x\chromedriver.exe
${STRING}   secret_sauce
@{LIST}     standard_user   locked_out_user     problem_user    performance_glitch_user     error_user      visual_user
&{DICT}     string=${STRING}    list=@{LIST}


*** Test Cases ***

LoginTest
    create webdriver    chrome  executable_path="xx-x-x--x\chromedriver.exe"
    Open browser    ${url}  ${browser}
    maximize browser window

Loop_a_DICT
    Log     ${DICT}
    FOR     ${key_value_tuple}     IN      @{DICT} 
        Log     ${key}=${DICT}[${key}]
        input text      id:user-name    ${key}
        input text      id:password     ${STRING}
    END
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
