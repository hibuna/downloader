from typing import Annotated

from litestar.params import Body

from src.api.request import RequestDownloadUrl


request_download_url_type_title = "Download from URL"
request_download_url_type_description = (
    "Pass a valid URL to download the file directly from the host server."
)
RequestDownloadUrlType = Annotated[
    RequestDownloadUrl,
    Body(
        title=request_download_url_type_title,
        description=request_download_url_type_description,
    ),
]
