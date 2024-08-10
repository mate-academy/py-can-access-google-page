from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> mock.MagicMock:
    with mock.patch("app.main.valid_google_url") as mocked_func:
        yield mocked_func


@pytest.fixture()
def mocked_has_internet_connection() -> mock.MagicMock:
    with mock.patch("app.main.has_internet_connection") as mocked_func:
        yield mocked_func


@pytest.mark.parametrize(
    "valid_url, has_connection, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "should be 'Accessible' when url is valid and has connection",
        "should be 'Not accessible' when url is NOT valid and has connection",
        "should be 'Not accessible' when url is valid and has NO connection",
        ("should be 'Not accessible' when "
         "url is NOT valid and has NO connection"),
    ]
)
def test_can_access_google_page(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock,
        valid_url: bool,
        has_connection: bool,
        expected_result: str

) -> None:
    mocked_valid_google_url.return_value = valid_url
    mocked_has_internet_connection.return_value = has_connection
    assert can_access_google_page("valid_url") == expected_result
