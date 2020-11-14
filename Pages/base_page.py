from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Utils.Logs.logger import logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        try:
            self.wait_for_element(element).click()
            logger.info(f'Clicked on element {element}')
        except Exception:
            message = f"Clicking on element {element} failed"
            logger.exception(message)
            raise Exception(message)

    def js_click(self, element):
        web_element = self.wait_for_element(element)
        try:
            self.driver.execute_script("arguments[0].click();", web_element)
            logger.info(f'Clicked on element using javascript {element}')
        except Exception:
            message = f"js clicking on element {element} failed"
            logger.exception(message)
            raise Exception(message)

    def type(self, element, text):
        try:
            self.wait_for_element(element).send_keys(text)
            logger.info(f'Typed {text} in element {element}')
        except Exception:
            message = f"Typing in element {element} failed"
            logger.exception(message)
            raise Exception(message)

    def is_element_displayed(self, element):
        try:
            return bool(WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element)))
        except Exception:
            message = f"Element {element} is not displayed"
            logger.exception(message)
            raise Exception(message)

    def wait_for_element(self, element):
        try:
            return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        except Exception:
            message = f"Element {element} was not found"
            logger.exception(message)
            raise Exception(message)

    def get_page_title(self):
        logger.info(f'Page title is "{self.driver.title}"')
        return self.driver.title

    def get_page_url(self):
        logger.info(f'Page URL is "{self.driver.current_url}"')
        return self.driver.current_url
