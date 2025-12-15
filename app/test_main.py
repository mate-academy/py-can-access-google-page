from app.main import can_access_google_page
from unittest.mock import MagicMock
from unittest import mock
import pytest


@pytest.fixture()
def url() -> str:
    return "http://google.com.ua"


@mock.patch("app.main.valid_google_url")
def test_mocked_valid_google_url(mocked_valid_google_url2: MagicMock,
                                 url: str) -> None:
    mocked_valid_google_url2(url)
    mocked_valid_google_url2.assert_called_once_with(url)


@mock.patch("app.main.has_internet_connection")
def test_mocked_has_internet_connection(
        mocked_has_internet_connection2: MagicMock, url: str) -> None:
    can_access_google_page(url)
    mocked_has_internet_connection2.assert_called_once()


@pytest.mark.parametrize(
    "valid_google_url_return,has_internet_connection_return,result",
    [
        pytest.param(True, True, "Accessible",
                     id="test_if_two_dependencies_are_True"),
        pytest.param(True, False, "Not accessible",
                     id="test_cannot_access_if_only_url"),
        pytest.param(False, True, "Not accessible",
                     id="test_cannot_access_if_only_connection"),
        pytest.param(False, False, "Not accessible",
                     id="test_if_two_dependencies_are_False")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mocked_valid_google_url2: MagicMock,
                                mocked_has_internet_connection2: MagicMock,
                                valid_google_url_return: bool,
                                has_internet_connection_return: bool,
                                result: str, url: str) -> None:
    mocked_valid_google_url2.return_value = valid_google_url_return
    mocked_has_internet_connection2.return_value = (
        has_internet_connection_return)
    assert can_access_google_page(url) == result
