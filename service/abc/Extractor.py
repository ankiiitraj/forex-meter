
from abc import ABC, abstractmethod


class Extractor(ABC):
    extraction: dict

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def extract(self, text: str) -> dict:
        pass

    