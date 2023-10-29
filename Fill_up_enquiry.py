*** Settings ***

Library SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}      xx-x-x--x\chromedriver.exe
${STRING}   secret_sauce
${FILL_STRING}  sk@gmail.com    shubham     katare      xyz     xx-xxxxxxx      INDIA
@{LIST}     standard_user   locked_out_user     problem_user    performance_glitch_user     error_user      visual_user
&{DICT}     string=${STRING}    list=@{LIST}
@{HAMB_LIST}     ALL Items      About     Logout    Reset App State
&{HAMB_DICT}     string=${HAMB_URL}    list=@{HAMB_LIST}
&{about}    //img[@alt='Saucelabs']
@{FILL_LIST}        //*[@id="Email"]    //*[@id="FirstName"]    //*[@id="LastName"]     //*[@id="Company"]      //*[@id="Phone"]    //*[@id="Country"]  
&{FILL_DICT}        string=${FILL_STRING}       list=@{FILL_LIST}

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
     
     click element       xpath://button[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButton-outlinedDark MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-disableElevation MuiButton-root MuiButton-outlined MuiButton-outlinedDark MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-disableElevation css-1r365wf']
     
     sleep  5 
     
     element should be visible      xpath://*[@id="mktoForm_3124"]/div[1]/div[1]/div[2]/div[1]/span
     
LOOP_FOR_FILL_DETAILS
    
    LOG     FILL_DETAILS 
    
    FOR     ${key_value_tuple}     IN      @{FILL_DICT} 
        Log     ${key}=${FILL_DICT}[${key}]
        IF      ${FILL_LIST:0} != ${FILL_STRING:0}
            exception  "Must be valid email"
        ELIF    ${FILL_LIST:1} != ${FILL_STRING:1}
            exception   "This field is required"
        ELIF    ${FILL_LIST:2} != ${FILL_STRING:2}
            exception   "This field is required"
        ELIF    ${FILL_LIST:3} != ${FILL_STRING:3}
            exception   "This field is required"
        ELIF    ${FILL_LIST:4} != ${FILL_STRING:4}
            exception   "This field is required"
        ELIF    ${FILL_LIST:5} != ${FILL_STRING:5}
            exception   "Must be a phone number.503-555-1212"
        ELIF    ${FILL_LIST:6} != ${FILL_STRING:6}
            exception   "This field is required"
        ELSE
            input text      ${FILL_STRING}      ${FILL_LIST}
    END
    click element   xpath://input[@id='login-button']
    
    close browser
