
from abc import ABC, abstractmethod


class Downloader(ABC):
    url: str
    dest: str

    @abstractmethod
    def __init__(self, url, dest):
        pass

    @abstractmethod
    def download():
        pass
