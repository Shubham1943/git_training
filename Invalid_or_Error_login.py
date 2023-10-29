
*** Settings ***

Library SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}      xx-x-x--x\chromedriver.exe
${STRING}   secret_sauce
@{LIST}     standard_user   locked_out_user     problem_user    performance_glitch_user     error_user      visual_user
&{DICT}     string=${STRING}    list=@{LIST}


*** Test Cases ***

InvvalidLoginTest
    create webdriver    chrome  executable_path="xx-x-x--x\chromedriver.exe"
    Open browser    ${url}  ${browser}
    maximize browser window

    Log     ${DICT}
    FOR     ${key_value_tuple}     IN      @{DICT} 
        Log     ${key}=${DICT}[${key}]
        IF      ${DICT}      IN      ${LIST} == none:
            LOG     "Username is required"
        ELIF    ${key}   IN      ${STRING} == none:
            LOG     "Password is required"
        ELSE
            LOG     "INVALID CREDENTIAL"
        
    END
    
    sleep   5
    
    close browser    
