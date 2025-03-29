from functools import cached_property

from src.downloader.provider import ServiceProvider


class Kernel:
    @cached_property
    def service(self) -> "ServiceProvider":
        return ServiceProvider()


app = Kernel()
