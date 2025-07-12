from unittest.mock import patch, MagicMock

from pytest import fixture

from app.main import can_access_google_page


@fixture
def mocked_url() -> MagicMock:
    with patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


@fixture()
def mocked_internet() -> MagicMock:
    with patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_can_access_google_page_valid_url_and_has_connection(
        mocked_url: MagicMock,
        mocked_internet: MagicMock
) -> None:
    mocked_url.return_value = True
    mocked_internet.return_value = True
    assert can_access_google_page("http://example.com") == "Accessible"


def test_can_access_google_page_not_valid_url_and_has_connection(
        mocked_url: MagicMock,
        mocked_internet: MagicMock
) -> None:
    mocked_url.return_value = False
    mocked_internet.return_value = True
    assert can_access_google_page("http://example.com") == "Not accessible"


def test_can_access_google_page_valid_url_and_has_no_connection(
        mocked_url: MagicMock,
        mocked_internet: MagicMock
) -> None:
    mocked_url.return_value = True
    mocked_internet.return_value = False
    assert can_access_google_page("http://example.com") == "Not accessible"


def test_can_access_google_page_not_valid_url_and_has_no_connection(
        mocked_url: MagicMock,
        mocked_internet: MagicMock
) -> None:
    mocked_url.return_value = False
    mocked_internet.return_value = False
    assert can_access_google_page("http://example.com") == "Not accessible"
