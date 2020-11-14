from enum import Enum


class SupportedBrowsers(Enum):
    # Enum's names are not written in capital letters in order to be compatible with Selenoid.
    chrome = 1
    firefox = 2
    MicrosoftEdge = 3
