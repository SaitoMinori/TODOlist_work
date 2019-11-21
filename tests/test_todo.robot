*** Settings ***
Documentation  テスト
Library   SeleniumLibrary

*** Test Cases ***
local todolistの確認テスト
    Set Selenium Speed      0.2s
    Open Browser  http://127.0.0.1:5000/  Chrome

    Click Element       name=submit
    Page Should Contain    No input!!

    Input Text  name=title    listen to music
    Click Element       name=submit
    Page Should Not Contain    No input!!

    Click Element       id=1

    ${value} =    Get Text    //html/body/form[2]/ul/li[1]
    Should Be Equal            ${value}      write article [delete]
    Log To Console  ${value}

    ${value} =    Get Text    //html/body/form[2]/ul/li[2]
    Should Be Equal            ${value}      eat cake [delete]
    Log To Console  ${value}

    ${value} =    Get Text    //html/body/form[2]/ul/li[3]
    Should Be Equal            ${value}      listen to music [delete]
    Log To Console  ${value}
   
    select checkbox  name=2
    select checkbox  name=3
    select checkbox  name=4
    Click Element       name=delete all
    Page Should Contain    you can register something to do.


