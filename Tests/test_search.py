import allure
from Pages.home_page import HomePage
from Tests.test_base import TestBase


class TestSearch(TestBase):
    SEARCH_ITEM = TestBase.get_data('searchItem')

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Searching for an item and checking that all search results match search criteria')
    def test_if_search_results_are_correct(self, init_driver):
        home_page = HomePage(init_driver)
        search_page = home_page.search_items(self.SEARCH_ITEM)
        assert search_page.are_search_results_correct(self.SEARCH_ITEM), "Search results are incorrect"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Searching for an item and adding it to the cart')
    def test_add_item_to_cart(self, init_driver):
        home_page = HomePage(init_driver)
        search_page = home_page.search_items(self.SEARCH_ITEM)
        search_page.add_item_to_cart()
        assert search_page.is_added_to_cart_notification_displayed(), "Item was not added to cart"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Searching for an item and adding it to products comparison')
    def test_add_item_to_compare(self, init_driver):
        home_page = HomePage(init_driver)
        search_page = home_page.search_items(self.SEARCH_ITEM)
        search_page.add_item_to_compare()
        assert search_page.is_added_to_compare_notification_displayed(), "Item was not added to comparison"
