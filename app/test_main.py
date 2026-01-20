from unittest import mock
import pytest


from app.main import can_access_google_page


@pytest.fixture()
def get_link() -> str:
    return "https://www.google.com/webhp?client=firefox-b-d"


@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection_call(mocked: mock.MagicMock,
                                      get_link: str) -> None:
    can_access_google_page(get_link)
    try:
        mocked.assert_called_once()
    except AssertionError:
        raise AssertionError("Function can_access_google_page was not called")


@mock.patch("app.main.valid_google_url")
def test_have_valid_google_url(mocked: mock.MagicMock, get_link: str) -> None:
    can_access_google_page(get_link)
    try:
        mocked.assert_called_once_with(get_link)
    except AssertionError:
        raise AssertionError(f"This page {get_link} was not opened")


@pytest.mark.parametrize(
    "has_connect, valid_page, result", [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ], ids=[
        "All is fine",
        "Wrong page",
        "No connection",
        "No connection and Wrong page"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_combination_of_returns(mock_connect: mock.MagicMock,
                                mock_valid: mock.MagicMock,
                                has_connect: bool,
                                valid_page: bool,
                                result: str,
                                get_link: str) -> None:
    mock_connect.return_value = has_connect
    mock_valid.return_value = valid_page
    assert can_access_google_page(get_link) == result
