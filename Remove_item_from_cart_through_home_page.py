*** Settings ***
Library SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  xx-x-x--x\chromedriver.exe
@{cart_item}    add-to-cart-sauce-labs-backpack     add-to-cart-sauce-labs-bike-light       add-to-cart-sauce-labs-bolt-t-shirt     add-to-cart-sauce-labs-fleece-jacket        add-to-cart-sauce-labs-onesie       add-to-cart-test.allthethings()-t-shirt-(red)
${string_condition}     Remove
*** Test Cases ***
add_to_cart
    create webdriver    chrome  executable_path="xx-x-x--x\chromedriver.exe"
    Open browser    ${url}  ${browser}
    maximize browser window
    input text      id:user-name    standard_user
    input text      id:password     secret_sauce
    click element   xpath://input[@id='login-button']
    
    FOR     ${ITEM}     IN      @{CART_ITEM}
        
        IF   "${string_condition}" == "Remove"
            click element   ${ITEM}
            LOG     "ITEM REMOVED FROM CART"
    END 
    
    click element   xpath://a[@class='shopping_cart_link']
    
    title should be     'Your Cart'
    
    click element   xpath://input[@id='//continue-shopping']
