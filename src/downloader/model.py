from pydantic import BaseModel, Field

from src.downloader.enumeration import EnumDownloaderInputResourceType


class Dto(BaseModel):
    pass


class InputModel(Dto):
    resource_handle: str = Field()
    resource_type: EnumDownloaderInputResourceType


class InputUrlModel(InputModel):
    resource_type: EnumDownloaderInputResourceType = EnumDownloaderInputResourceType.URL
