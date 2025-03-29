from abc import abstractmethod, ABC

from src.downloader.model import InputUrlModel, Dto
from src.logger import log_transform


class PostprocessorBase(ABC):
    output_type: Dto

    @abstractmethod
    @log_transform
    def process(self, request) -> Dto: ...

    @abstractmethod
    def _create_dto(self, *args, **kwargs) -> Dto: ...


class PostprocessorRequestDownloadUrl(PostprocessorBase):
    output_type = InputUrlModel

    @log_transform
    def process(self, dto: InputUrlModel) -> InputUrlModel:
        return self._create_dto(handle=dto.resource_handle)

    def _create_dto(self, handle: str) -> InputUrlModel:
        return InputUrlModel(resource_handle=handle)
