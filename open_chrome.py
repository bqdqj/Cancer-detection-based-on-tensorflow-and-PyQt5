from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import chromedriver_path, url


class Chrome:
    def __init__(self):
        self.chromedriver_path = chromedriver_path
        self.url = url
        self.options = Options()
        self.driver = webdriver.Chrome(options=self.options, executable_path=self.chromedriver_path)

        self.open_page()

    def open_page(self):
        self.driver.get(self.url)