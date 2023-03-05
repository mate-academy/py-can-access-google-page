from app.main import can_access_google_page
import pytest
from unittest import mock


url = "https://www.google.com"


@pytest.fixture()
def mock_called() -> mock:
    with (
            mock.patch("app.main.valid_google_url") as valid_url,
            mock.patch("app.main.has_internet_connection") as connection
    ):
        yield [valid_url, connection]


def test_can_access_google_page_request(mock_called: mock) -> None:
    mock_called[0].return_value = True
    mock_called[1].return_value = True
    assert can_access_google_page(url) == "Accessible"


def test_error_url(mock_called: mock) -> None:
    mock_called[0].return_value = False
    mock_called[1].return_value = True
    assert can_access_google_page(url) == "Not accessible"


def test_error_date(mock_called: mock) -> None:
    mock_called[0].return_value = True
    mock_called[1].return_value = False
    assert can_access_google_page(url) == "Not accessible"


def test_error_date_and_url(mock_called: mock) -> None:
    mock_called[0].return_value = False
    mock_called[1].return_value = False
    assert can_access_google_page(url) == "Not accessible"
