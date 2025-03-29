from functools import cached_property


class ServiceProvider:
    @cached_property
    def download(self):
        from src.downloader.service import DownloadServiceController

        return DownloadServiceController()

    @cached_property
    def download_url(self):
        from src.downloader.service import DownloadServiceUrl

        return DownloadServiceUrl()
