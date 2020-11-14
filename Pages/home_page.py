from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Pages.search_page import SearchPage


class HomePage(BasePage):
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".search-box-button")

    def search_items(self, text):
        self.type(self.SEARCH_INPUT, text)
        self.click(self.SEARCH_BUTTON)
        return SearchPage(self.driver)

    def get_home_page_title(self):
        return self.get_page_title()
