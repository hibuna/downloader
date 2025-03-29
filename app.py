from litestar import Litestar

from src.api.controller import ApiControllerDownload


litestar_app = Litestar([ApiControllerDownload])
