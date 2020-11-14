from Config.Browsers.chrome_browser import ChromeBrowser
from Config.Browsers.edge_browser import EdgeBrowser
from Config.Browsers.firefox_browser import FirefoxBrowser
from Config.Browsers.supported_browsers import SupportedBrowsers


class BrowserFactory:
    @staticmethod
    def get_browser(config_browser):
        if config_browser == SupportedBrowsers.chrome.name:
            return ChromeBrowser()
        elif config_browser == SupportedBrowsers.firefox.name:
            return FirefoxBrowser()
        else:
            return EdgeBrowser()
