from selenium.webdriver.common.by import By
from Utils.Logs.logger import logger
from Pages.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_ITEMS = (By.CLASS_NAME, "product-title")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "input[value='Add to cart']")
    ADDED_TO_CART_NOTIFICATION = (By.XPATH, "//a[text()= 'shopping cart']")
    ADD_TO_COMPARE_BUTTON = (By.CSS_SELECTOR, "input[value='Add to compare list']")
    ADDED_TO_COMPARE_NOTIFICATION = (By.XPATH, "//a[text()= 'product comparison']")

    def are_search_results_correct(self, text):
        search_results = self.driver.find_elements(*self.SEARCH_ITEMS)
        if not search_results:
            message = "There are no results matching the search criteria"
            logger.error(message)
            raise Exception(message)
        return all(text in item.text.lower() for item in search_results)

    def add_item_to_cart(self):
        self.js_click(self.ADD_TO_CART_BUTTON)

    def is_added_to_cart_notification_displayed(self):
        return self.is_element_displayed(self.ADDED_TO_CART_NOTIFICATION)

    def add_item_to_compare(self):
        self.js_click(self.ADD_TO_COMPARE_BUTTON)

    def is_added_to_compare_notification_displayed(self):
        return self.is_element_displayed(self.ADDED_TO_COMPARE_NOTIFICATION)
