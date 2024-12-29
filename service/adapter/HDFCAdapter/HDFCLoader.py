
import sys
from service.abc.Loader import Loader


class HDFCLoader(Loader):

    def __init__(self):
        pass

    def save(self, payload: dict) -> None:
        frame = sys._getframe().f_code.co_name
        print(__name__ + " " + frame)

    def load(self) -> dict:
        pass
