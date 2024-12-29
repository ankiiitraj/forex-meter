
import sys
from service.abc.Transformer import Transformer


class HDFCTransformer(Transformer):

    def __init__(self):
        pass

    def transform(self, payload: dict) -> dict:
        frame = sys._getframe().f_code.co_name
        print(__name__ + " " + frame)