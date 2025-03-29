from dataclasses import dataclass


@dataclass
class BaseRequest:
    pass


@dataclass
class RequestDownload(BaseRequest):
    handle: str


@dataclass
class RequestDownloadUrl(RequestDownload):
    handle: str
