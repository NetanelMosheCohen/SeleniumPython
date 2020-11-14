from Config.Browsers.browser import Browser
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class FirefoxBrowser(Browser):
    @classmethod
    def init_browser(cls):
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())

