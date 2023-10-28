*** Settings ***

Library SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  xx-x-x--x\chromedriver.exe

*** Test Cases ***
SortingTest

    Open browser    ${url}  ${browser}
    maximize browser window
    
    select from list by value   xpath://select[@class='product_sort_container']     az
    sleep   5
    select from list by value   xpath://select[@class='product_sort_container']     za
    sleep   5
    select from list by value   xpath://select[@class='product_sort_container']     lohi
    sleep   5
    select from list by value   xpath://select[@class='product_sort_container']     hilo
    close browser
    
