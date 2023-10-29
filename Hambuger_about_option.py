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
&{about}    //img[@alt='Saucelabs']

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
    
Hamburger_about_option

     Log     ${HAMB_DICT}
     
     click element      xpath://*[@id="react-burger-menu-btn"]
     
     click element      xpath://*[@id="about_sidebar_link"]   
     
     sleep  5
     
     element should be visible      &{about}
     
     
     Log    //img[@alt='Saucelabs']
     
     close browser
     
