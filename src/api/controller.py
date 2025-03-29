from litestar import Controller, post
from src.api.type import RequestDownloadUrlType
from src.downloader import downloader
from src.middleware import middleware


class ApiController(Controller):
    pass


class ApiControllerDownload(ApiController):
    path = "/download"

    @post("/url")
    async def handler(self, data: RequestDownloadUrlType) -> None:
        dto_input = middleware.service.preprocess_service_url.process(data)
        dto_output = downloader.service.download.download(dto_input)
        return dto_output
