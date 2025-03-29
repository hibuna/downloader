import enum


class EnumBase(int, enum.Enum):
    pass


class EnumDownloaderInputResourceType(EnumBase):
    URL = 1
