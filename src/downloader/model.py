from src.downloader.enumeration import EnumDownloaderInputResourceType


class BaseModel:
    pass


class Dto(BaseModel):
    pass


class InputModel(Dto):
    resource_handle: str
    resource_type: EnumDownloaderInputResourceType

    def __init__(self, resource_handle: str):
        self.resource_handle = resource_handle


class InputUrlModel(InputModel):
    resource_type = EnumDownloaderInputResourceType.URL
