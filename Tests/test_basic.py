import allure
from Pages.home_page import HomePage
from Tests.test_base import TestBase


class TestBasic(TestBase):
    APP_TITLE = TestBase.get_data('appTitle')
    APP_URL = TestBase.get_data('baseUrl')

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.description('Checking that app title is correct')
    def test_if_site_title_is_correct(self, init_driver):
        home_page = HomePage(init_driver)
        actual_title = home_page.get_home_page_title()
        assert actual_title == self.APP_TITLE, "App title is incorrect"

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.description('Checking that app URL is correct')
    def test_if_site_url_is_correct(self, init_driver):
        home_page = HomePage(init_driver)
        actual_url = home_page.get_page_url()
        assert actual_url == self.APP_URL, "App URL is incorrect"
