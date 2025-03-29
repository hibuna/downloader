from litestar import Litestar, get

from src.downloader.main import app as downloader_app
from src.downloader.model import InputUrlModel


@get("/")
async def index() -> str:
    return "Hello, world!"


@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


litestar_app = Litestar([index, get_book])

input_model = InputUrlModel(resource_handle="some_handle")
downloader_app.service.download.download(input_model)
