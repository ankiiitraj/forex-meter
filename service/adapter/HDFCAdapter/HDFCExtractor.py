
import sys
from service.abc.Extractor import Extractor


class HDFCExtractor(Extractor):
    extraction: dict

    def __init__(self):
        pass

    def extract(self, text: str) -> dict:
        frame = sys._getframe().f_code.co_name
        print(__name__ + " " + frame)

    