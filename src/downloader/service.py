from abc import ABC, abstractmethod

from src.downloader import downloader
from src.downloader.enumeration import EnumDownloaderInputResourceType
from src.downloader.exception import EnumUnexpectedValueException
from src.downloader.model import InputModel, InputUrlModel


class Service:
    pass


class DownloadServiceController(Service):
    def download(self, resource: InputModel):
        service = self._determine_service(resource=resource)
        return service.download(resource=resource)

    def _determine_service(self, resource: InputModel) -> "DownloadService":
        match resource.resource_type:
            case EnumDownloaderInputResourceType.URL:
                return downloader.service.download_service_url

        raise EnumUnexpectedValueException(resource.resource_type)


class DownloadService(ABC):
    @abstractmethod
    def download(self, resource: InputModel): ...


class DownloadServiceUrl(DownloadService):
    def download(self, resource: InputUrlModel):
        print("Success!")
