from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mock_has_internet() -> None:
    with mock.patch(
            "app.main.has_internet_connection"
    ) as mocked_has_internet_connection:
        yield mocked_has_internet_connection


@pytest.fixture()
def mock_has_url() -> None:
    with mock.patch(
            "app.main.valid_google_url"
    ) as mocked_google_url:
        yield mocked_google_url


@pytest.mark.parametrize(
    "mocked_has_internet_connection,"
    "mocked_google_url,"
    "expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible")
    ],
    ids=[
        "if correct url and correct_time",
        "if not correct url but correct time",
        "if not correct url and has not internet connection",
        "if correct url and not correct time"
    ]
)
def test_can_access_google_page(
        mock_has_internet: None,
        mock_has_url: None,
        mocked_has_internet_connection: bool,
        mocked_google_url: bool,
        expected: str
) -> None:
    mock_has_internet.return_value = mocked_has_internet_connection
    mock_has_url.return_value = mocked_google_url
    assert can_access_google_page("http://www.google.com") == expected
