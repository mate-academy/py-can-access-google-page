from requests.exceptions import MissingSchema
from app.main import can_access_google_page
from unittest import mock
import pytest


@pytest.fixture()
def mock_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mock_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_internet:
        yield mock_internet


def test_accessible(mock_valid_url: str, mock_connection: int) -> None:
    mock_valid_url.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("https://github.com/") == "Accessible"


def test_not_accessible_url(
        mock_valid_url: str, mock_connection: int
) -> None:
    mock_valid_url.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page("https://github.com/") ==\
           "Not accessible"


def test_not_accessible_connection(
        mock_valid_url: str, mock_connection: int
) -> None:
    mock_valid_url.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page("https://github.com/") ==\
           "Not accessible"


def test_not_accessible(
        mock_valid_url: str, mock_connection: int
) -> None:
    mock_valid_url.return_value = False
    mock_connection.return_value = False
    assert can_access_google_page("https://github.com/") ==\
           "Not accessible"


def test_valid_url_and_connection(
        mock_valid_url: str, mock_connection: int
) -> None:
    can_access_google_page("https://github.com/")
    mock_valid_url.assert_called_once()
    mock_connection.assert_called_once()


def test_raise_missing_schema(mock_connection: int) -> None:
    with pytest.raises(MissingSchema):
        can_access_google_page(23)
