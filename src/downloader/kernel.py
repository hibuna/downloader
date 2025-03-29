from functools import cached_property


class Kernel:
    @cached_property
    def service(self) -> "ServiceProvider":
        return ServiceProvider()


class ServiceProvider:
    @cached_property
    def download(self):
        from src.downloader.service import DownloadServiceController

        return DownloadServiceController()

    @cached_property
    def download_service_url(self):
        from src.downloader.service import DownloadServiceUrl

        return DownloadServiceUrl()
