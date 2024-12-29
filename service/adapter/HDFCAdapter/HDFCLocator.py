
import sys
from service.abc.Locator import Locator


class HDFCLocator(Locator):
    url: str

    def __init__(self, url):
        self.url = url

    def locate(self) -> str:
        frame = sys._getframe().f_code.co_name
        print(__name__ + " " + frame)

