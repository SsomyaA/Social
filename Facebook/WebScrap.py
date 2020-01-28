from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from time import sleep

class WbScrapApp():

    def __init__(self, username= "Somya", password = "Biswal"):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('/Users/somyabiswal/Documents/Project/Social/chromedriver')
        self.mailUrl = 'https://www.facebook.com/'
        self.driver.get(self.mailUrl)


if __name__ == "__main__":
    WbScrapApp()