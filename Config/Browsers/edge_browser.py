from Config.Browsers.browser import Browser
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class EdgeBrowser(Browser):
    @classmethod
    def init_browser(cls):
        return webdriver.Edge(EdgeChromiumDriverManager().install())
