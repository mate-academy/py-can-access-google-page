from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def mocked_valid_google_url() -> mock.MagicMock:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


@pytest.fixture
def mocked_has_internet_connection() -> mock.MagicMock:
    with mock.patch("app.main.has_internet_connection") as mocked_has_connect:
        yield mocked_has_connect


@pytest.mark.parametrize(
    "url_correct, internet_connection, can_access",
    [
        pytest.param(False, True, "Not accessible",
                     id="Not valid url"),
        pytest.param(True, False, "Not accessible",
                     id="No internet connection"),
        pytest.param(True, True, "Accessible",
                     id="Correct url and internet connection for access"),
        pytest.param(False, False, "Not accessible",
                     id="Not valid url and internet connection")
    ]
)
def test_can_access_google_page(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock,
        url_correct: bool,
        internet_connection: bool,
        can_access: str
) -> None:
    mocked_valid_google_url.return_value = url_correct
    mocked_has_internet_connection.return_value = internet_connection
    assert can_access_google_page("https://google.com") == can_access
