from abc import abstractmethod, ABC


class Browser(ABC):
    @abstractmethod
    def init_browser(self):
        pass
