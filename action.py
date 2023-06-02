import Speechtotext
import Texttospeech
from selenium import webdriver
import wikipedia
import time
from youtube_search import YoutubeSearch
from selenium.webdriver.common.keys import Keys
import webbrowser
import os
wikipedia.set_lang('vi')
language = 'vi'

def open_google_and_search():
    Texttospeech.text_speech("Bạn muốn tìm gì?")
    time.sleep(7)
    my = Speechtotext.speech_text()
    print(my)
    url = 'https://www.google.com/search?q='+my
    driver=webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)

open_google_and_search()