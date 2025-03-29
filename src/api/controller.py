import logging
from typing import Any

from litestar import Controller, post
from src.api.type import RequestDownloadUrlType
from src.downloader.service import DownloadServiceController
from src.middleware import middleware
from src.middleware.postprocessor import PostprocessorBase
from src.middleware.preprocessor import PreprocessorBase


class ApiController(Controller):
    pass


class ApiControllerDownload(ApiController):
    preprocessor: PreprocessorBase
    postprocessor: PostprocessorBase
    downloader = DownloadServiceController()

    def handle(self, data: Any) -> Any:
        logging.info("START: " + __name__ + " " + self.__class__.__name__)

        data = self._preprocess(data)
        data = self._process(data)
        if data is not None:
            data = self._process(data)

        logging.info("END: " + __name__ + " " + self.__class__.__name__)
        return data

    def _preprocess(self, data: Any) -> Any:
        logging.info("PREPROCESS - START")
        result = self.preprocessor.process(data=data)
        logging.info("PREPROCESS - END")
        return result

    def _process(self, data: Any) -> Any:
        logging.info("PROCESS - START")
        result = self.downloader.download(data)
        logging.info("PROCESS - END")
        return result

    def _postprocess(self, data: Any) -> Any:
        logging.info("POSTPROCESS - START")
        result = self.postprocessor.process(data=data)
        logging.info("POSTPROCESS - END")
        return result


class ApiControllerDownloadUrl(ApiControllerDownload):
    path = "/download"
    preprocessor = middleware.service.preprocess_download_url
    postprocessor = middleware.service.postprocess_download_url

    @post("/url")
    async def handle(self, data: RequestDownloadUrlType) -> None:
        return super().handle(data)
