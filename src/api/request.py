from pydantic import BaseModel


class BaseRequest(BaseModel):
    pass


class RequestDownload(BaseRequest):
    handle: str


class RequestDownloadUrl(RequestDownload):
    handle: str
