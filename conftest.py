import json
import pytest
from selenium import webdriver
from Config.Browsers.browser_factory import BrowserFactory
from Config.Browsers.supported_browsers import SupportedBrowsers
from Config.Platforms.supported_platforms import SupportedPlatforms
from Utils.Logs.logger import logger
import allure

from Tests.test_base import TestBase

CONFIG_PATH = 'Config/config.json'


@pytest.fixture(scope='session', autouse=True)
def read_config_file():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    logger.info("Read configuration file")
    return data


@pytest.fixture(scope='session')
def config_platform(read_config_file):
    # Validate and return the platform choice (grid or local) from the config file
    if 'platform' not in read_config_file:
        error = 'The config file does not contain "platform"'
        logger.error(error)
        raise Exception(error)
    elif read_config_file['platform'].upper() not in SupportedPlatforms.__members__:
        error = f'"{read_config_file["platform"]}" is not a supported platform'
        logger.error(error)
        raise Exception(error)
    logger.info(f"{read_config_file['platform']} platform configured")
    return read_config_file['platform']


@pytest.fixture(scope='session')
def config_browser(read_config_file):
    # Validate and return the browser choice from the config data
    if 'browser' not in read_config_file:
        error = 'The config file does not contain "browser"'
        logger.error(error)
        raise Exception(error)
    elif read_config_file['browser'] not in SupportedBrowsers.__members__:
        error = f'"{read_config_file["browser"]}" is not a supported browser'
        logger.error(error)
        raise Exception(error)
    logger.info(f"{read_config_file['browser']} browser configured")
    return read_config_file['browser']


@pytest.fixture()
def init_driver(read_config_file, config_platform, config_browser, request):
    if config_platform.upper() == SupportedPlatforms.GRID.name:
        driver = webdriver.Remote(
            command_executor=read_config_file["remoteUrl"],
            desired_capabilities={"browserName": config_browser, "selenoid:options": {"enableVNC": True}}
        )

    else:
        browser = BrowserFactory.get_browser(config_browser)
        driver = browser.init_browser()

    logger.info("Driver was initialized")
    driver.maximize_window()
    logger.info("Browser's window was maximized")
    driver.get(TestBase.get_data('baseUrl'))
    logger.info(f"Navigated to {TestBase.get_data('baseUrl')}")

    yield driver

    if request.node.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name=f"screenshot_{request.node.name}")
        logger.info(f"Screenshot was taken for test {request.node.name}")

    if driver:
        driver.quit()
        logger.info("Driver was closed")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
