from abc import abstractmethod, ABC

from src.api.request import RequestDownloadUrl
from src.downloader.model import InputUrlModel, Dto


class PreprocessorBase(ABC):
    output_type: Dto

    @abstractmethod
    def process(self, request) -> Dto: ...

    @abstractmethod
    def _create_dto(self, *args, **kwargs) -> Dto: ...


class PreprocessorRequestDownloadUrl(PreprocessorBase):
    output_type = InputUrlModel

    def process(self, request: RequestDownloadUrl) -> InputUrlModel:
        return self._create_dto(handle=request.handle)

    def _create_dto(self, handle: str) -> InputUrlModel:
        return self.output_type(resource_handle=handle)