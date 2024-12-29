
from service.abc.Downloader import Downloader 
from service.abc.Extractor import Extractor 
from service.abc.Loader import Loader 
from service.abc.Transformer import Transformer 
from service.abc.Locator import Locator 
from service.abc.Adapter import Adapter
from service.adapter.HDFCAdapter.HDFCDownloader import HDFCDownloader
from service.adapter.HDFCAdapter.HDFCExtractor import HDFCExtractor
from service.adapter.HDFCAdapter.HDFCLocator import HDFCLocator
from service.adapter.HDFCAdapter.HDFCLoader import HDFCLoader
from service.adapter.HDFCAdapter.HDFCTransformer import HDFCTransformer


class HDFCAdapter(Adapter):
    locator: Locator
    downloader: Downloader
    extractor: Extractor
    loader: Loader
    transformer: Transformer

    def __init__(self):
        self.downloader = HDFCDownloader("", "")
        self.extractor = HDFCExtractor()
        self.loader = HDFCLoader()
        self.transformer = HDFCTransformer()
        self.locator = HDFCLocator("")
