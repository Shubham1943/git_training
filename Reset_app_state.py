
*** Settings ***

Library SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}      xx-x-x--x\chromedriver.exe
${STRING}   secret_sauce
@{LIST}     standard_user   locked_out_user     problem_user    performance_glitch_user     error_user      visual_user
&{DICT}     string=${STRING}    list=@{LIST}
@{HAMB_LIST}     ALL Items      About     Logout    Reset App State
&{HAMB_DICT}     string=${HAMB_URL}    list=@{HAMB_LIST}


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
    
Hamburger_icon
     Log     ${HAMB_DICT}
     
     click element   xpath://*[@id="react-burger-menu-btn"]
     
     FOR     ${key_value_tuple}     IN      @{HAMB_DICT} 
     
        Log     ${key}=${HAMB_DICT}[${key}]
        
        IF      ${Reset App State}.click()    IN      ${HAMB_LIST}
            Log     "https://saucelabs.com/"
        ELSE 
            Log     "Error in loading"
     END
     
