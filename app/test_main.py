import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection, valid_google_url, result",
    [
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible"),
    ],
    ids=[
        "Not accessible: your URL is not valid",
        "Not accessible: you have no internet connection and URL",
        "Not accessible: your internet connection is disabled",
        "Accessible: your URL is valid and you have internet connection"
    ]
)
def test_can_access_google_page(
        has_internet_connection: bool,
        valid_google_url: bool,
        result: str
) -> None:
    with (mock.patch("app.main.valid_google_url",
                     return_value=valid_google_url),
          mock.patch("app.main.has_internet_connection",
                     return_value=has_internet_connection)):
        assert result == can_access_google_page("https://www.example.com")
