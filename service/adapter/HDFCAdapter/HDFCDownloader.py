
import sys
from service.abc.Downloader import Downloader


class HDFCDownloader(Downloader):
    url: str
    dest: str

    def __init__(self, url, dest):
        self.url = url
        self.dest = dest

    def download(self):
        frame = sys._getframe().f_code.co_name
        print(__name__ + " " + frame)
