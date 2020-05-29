*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
Library  news_rss_parser.py

*** Variables ***

*** Test Cases ***
OPEN ALL NEWS
    Define Keywords
    Get News
    Open Browser    File:///${CURDIR}\\..\\news.html  Firefox
    #click element   id:hissimusiikki
    click element   id:arvi