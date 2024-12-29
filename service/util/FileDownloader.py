from service.abc import Downloader
from service.logger import Logger
import requests

LOG = Logger.get_logger(__name__)

class FileDownloader(Downloader):

    def __init__(self, url: str, dest: str):
        self.url = url
        self.dest = dest

    def download(self):
        try:
            response = requests.get(self.url, stream=True)
            response.raise_for_status()

            with open(self.dest, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192): 
                    if chunk:
                        f.write(chunk)
            LOG.info(f"File downloaded successfully to {self.dest}")

        except requests.exceptions.RequestException as e:
            LOG.error(f"Error downloading file: {e}")
            raise e
