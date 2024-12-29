
from abc import ABC, abstractmethod


class Loader(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def save(self, payload: dict) -> None:
        pass

    @abstractmethod
    def load(self) -> dict:
        pass
