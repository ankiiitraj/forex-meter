
from abc import ABC, abstractmethod


class Transformer(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def transform(self, payload: dict) -> dict:
        pass