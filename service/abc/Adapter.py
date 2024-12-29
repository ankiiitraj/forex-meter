
from abc import ABC, abstractmethod
from service.abc import Downloader, Extractor, Loader, Transformer, Locator


class Adapter(ABC):
    downloader: Downloader
    extractor: Extractor
    loader: Loader
    transformer: Transformer
    locator: Locator

    @abstractmethod
    def __init__():
        pass

