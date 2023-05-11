from collections.abc import Generator
from typing import Callable
from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google_url() -> Generator[bool]:
    with mock.patch("app.main.valid_google_url") as valid_url:
        yield valid_url


@pytest.fixture()
def mock_has_internet_connection() -> Generator[bool]:
    with mock.patch("app.main.has_internet_connection") as internet_connection:
        yield internet_connection


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "valid_url, internet_connection, new_url, result",
        [
            pytest.param(
                True,
                True,
                "http:*//servername*",
                "Accessible",
                id="result should be Accessible"
            ),
            pytest.param(
                False,
                False,
                "http: * // servername:8080 / reportserver *",
                "Not accessible",
                id="result should be Not Accessible"
            ),
            pytest.param(
                True,
                False,
                "http: * // servername:8080 / reportserver *",
                "Not accessible",
                id="result should be Not Accessible"
            ),
            pytest.param(
                False,
                True,
                "http:*//servername*",
                "Not accessible",
                id="result should be Not Accessible"
            )
        ]
    )
    def test_can_access_google_page(
            self,
            valid_url: bool,
            internet_connection: bool,
            new_url: str,
            result: str,
            mock_valid_google_url: Callable,
            mock_has_internet_connection: Callable
    ) -> None:
        mock_valid_google_url.return_value = valid_url
        mock_has_internet_connection.return_value = internet_connection
        assert can_access_google_page(new_url) == result
