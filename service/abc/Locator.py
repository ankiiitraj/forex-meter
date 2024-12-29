
from abc import ABC, abstractmethod


class Locator(ABC):
    url: str

    @abstractmethod
    def __init__(self, url):
        pass

    @abstractmethod
    def locate(self) -> str:
        pass
