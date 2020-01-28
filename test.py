from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from time import sleep


driver = webdriver.Chrome('/Users/somyabiswal/Documents/Project/Social/chromedriver')
mailUrl = 'https://www.facebook.com/'
driver.get(mailUrl)