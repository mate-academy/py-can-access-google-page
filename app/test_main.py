import pytest

from unittest.mock import patch

from app.main import can_access_google_page


@pytest.fixture
def internet_true() -> bool:
    with patch("app.main.has_internet_connection", return_value=True):
        yield


@pytest.fixture
def internet_false() -> bool:
    with patch("app.main.has_internet_connection", return_value=False):
        yield


@pytest.fixture
def valid_url() -> bool:
    with patch("app.main.valid_google_url", return_value=True):
        yield


@pytest.fixture
def invalid_url() -> bool:
    with patch("app.main.valid_google_url", return_value=False):
        yield


def test_can_access_page_when_valid_url_and_has_internet(
        internet_true: bool,
        valid_url: bool
) -> None:
    assert can_access_google_page("https://google.com") == "Accessible"


def test_invalid_url_and_has_internet(
        internet_true: bool,
        invalid_url: bool
) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"


def test_no_internet_and_valid_url(
        internet_false: bool,
        valid_url: bool
) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"
