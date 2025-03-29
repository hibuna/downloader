from litestar import Litestar

from src.api.controller import ApiControllerDownloadUrl


litestar_app = Litestar([ApiControllerDownloadUrl])
