import unittest

from litestar.status_codes import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)
from litestar.testing import TestClient

from app import litestar_app


class TestApi(unittest.TestCase):
    def test_request_wrong_url(self):
        with TestClient(app=litestar_app) as client:
            response = client.post("/error", json={"handle": "some handle"})
            assert response.status_code == HTTP_404_NOT_FOUND

    def test_request_body_wrong_key(self):
        with TestClient(app=litestar_app) as client:
            response = client.post("/download/url", json={"error": "some handle"})
            assert response.status_code == HTTP_400_BAD_REQUEST

    def test_request_valid(self):
        with TestClient(app=litestar_app) as client:
            response = client.post("/download/url", json={"handle": "some handle"})
            assert response.status_code == HTTP_201_CREATED
