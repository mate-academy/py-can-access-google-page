from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid:
        yield mocked_valid


def test_if_valid_url_has_been_called(mocked_valid: callable) -> None:
    can_access_google_page("url")
    mocked_valid.assert_called_once_with("url")


def test_if_internet_connect_has_been_called(mocked_valid: callable) -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connect:
        can_access_google_page("url")
        mocked_connect.assert_called_once()
