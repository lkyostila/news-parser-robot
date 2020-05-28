*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
Library  news_rss_parser.py
*** Variables ***
${newsdir}
*** Test Cases ***
OPEN ALL NEWS
    get news
    open browser    File:///${CURDIR}\\..\\news.html  Chrome