from abc import abstractmethod, ABC

from src.api.request import RequestDownloadUrl
from src.downloader.model import InputUrlModel, Dto, InputModel
from src.logger import log_transform


class PreprocessorBase(ABC):
    output_type: Dto

    @abstractmethod
    @log_transform
    def process(self, request) -> InputModel: ...

    @abstractmethod
    def _create_dto(self, *args, **kwargs) -> Dto: ...


class PreprocessorRequestDownloadUrl(PreprocessorBase):
    output_type = InputUrlModel

    @log_transform
    def process(self, data: RequestDownloadUrl) -> InputUrlModel:
        return self._create_dto(handle=data.handle)

    def _create_dto(self, handle: str) -> InputUrlModel:
        return self.output_type(resource_handle=handle)
