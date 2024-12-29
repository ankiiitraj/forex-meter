
from service.abc.Adapter import Adapter


class SchduleRunner():

    def run(self, adaptor: Adapter):
        adaptor.locator.locate()
        adaptor.downloader.download()
        adaptor.extractor.extract("")
        adaptor.loader.save({})
        adaptor.transformer.transform({})