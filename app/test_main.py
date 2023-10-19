from unittest import mock
import pytest

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
def test_valid_google_url_was_called(
        mocked_valid_google_url: mock.MagicMock,
) -> None:

    can_access_google_page("https://www.google.com/")
    mocked_valid_google_url.assert_called_once()


@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection_was_called(
        mocked_has_internet_connection: mock.MagicMock,
) -> None:

    can_access_google_page("https://www.google.com/")
    mocked_has_internet_connection.assert_called_once()


@pytest.mark.parametrize(
    "result_valid_google_url,has_internet_connection,expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "should return Accessible when valid page and have connection",
        "should return Not accessible when valid page, not have connection",
        "should return Not accessible when not valid page, have connection",
        "should return Not accessible when not valid page, not have connection"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_able_access_to_page_with(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock,
        result_valid_google_url: bool,
        has_internet_connection: bool,
        expected_result: str
) -> None:
    page = "https://www.google.com/"
    mocked_valid_google_url.return_value = result_valid_google_url
    mocked_has_internet_connection.return_value = has_internet_connection
    assert can_access_google_page(page) == expected_result
