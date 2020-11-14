from Config.Browsers.browser import Browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ChromeBrowser(Browser):
    @classmethod
    def init_browser(cls):
        return webdriver.Chrome(executable_path=ChromeDriverManager().install())
