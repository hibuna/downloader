from functools import cached_property


class Kernel:
    @cached_property
    def service(self) -> "MiddlewareProvider":
        return MiddlewareProvider()


class MiddlewareProvider:

    @cached_property
    def preprocess_service_url(self):
        from src.middleware.preprocessor import PreprocessorRequestDownloadUrl

        return PreprocessorRequestDownloadUrl()
