*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
Library  news_rss_parser.py

*** Variables ***
${headlines}
*** Test Cases ***
OPEN ALL NEWS
    Define Keywords
    ${headlines}=    Get News
    Open Browser    File:///${CURDIR}\\..\\news.html  Chrome
    click element   id:arvi
    Execute Javascript    window.open('')
    Get Window Titles
    Select Window    title=undefined
    go to   https://translate.google.fi/?hl=fi#view=home&op=translate&sl=auto&tl=fi&text=${headlines}
    click element   css:.res-tts
    select window   title=arvinews