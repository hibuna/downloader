from src.downloader.enumeration import EnumBase


class ExceptionBase(Exception):
    pass


class EnumUnexpectedValueException(ExceptionBase):
    def __init__(self, enum_value: EnumBase):
        enum_class = enum_value.__class__
        super().__init__("Unexpected enum value for enum:", enum_class, enum_value.name)
