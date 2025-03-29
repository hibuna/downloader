from src.api.request import RequestDownloadUrl
from src.downloader.model import InputUrlModel


class PreprocessorBase:
    pass


class PreprocessorRequestDownloadUrl(PreprocessorBase):
    output_type = InputUrlModel

    def process(self, request: RequestDownloadUrl):
        return self.output_type(resource_handle=request.handle)
