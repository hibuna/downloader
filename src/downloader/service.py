from abc import ABC, abstractmethod

from src.downloader.main import app
from src.downloader.enumeration import EnumDownloaderInputResourceType
from src.downloader.exception import EnumUnexpectedValueException
from src.downloader.model import InputModel, InputUrlModel


class Service:
    pass


class DownloadServiceController(Service):
    @staticmethod
    def download(resource: InputModel):
        service = DownloadServiceController._determine_service(resource=resource)
        return service.download(resource=resource)

    @staticmethod
    def _determine_service(resource: InputModel) -> "DownloadService":
        match resource.resource_type:
            case EnumDownloaderInputResourceType.URL:
                return app.service.download_url

        raise EnumUnexpectedValueException(resource.resource_type)


class DownloadService(ABC):
    @staticmethod
    @abstractmethod
    def download(resource: InputModel): ...


class DownloadServiceUrl(DownloadService):
    @staticmethod
    def download(resource: InputUrlModel):
        print("Success!")
