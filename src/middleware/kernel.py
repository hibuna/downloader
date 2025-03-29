from functools import cached_property


class Kernel:
    @cached_property
    def service(self) -> "MiddlewareProvider":
        return MiddlewareProvider()


class MiddlewareProvider:
    @cached_property
    def preprocess_download_url(self):
        from src.middleware.preprocessor import PreprocessorRequestDownloadUrl

        return PreprocessorRequestDownloadUrl()

    @cached_property
    def postprocess_download_url(self):
        from src.middleware.postprocessor import PostprocessorRequestDownloadUrl

        return PostprocessorRequestDownloadUrl()
