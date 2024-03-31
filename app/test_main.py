from unittest import mock
import pytest


from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection_call(mocked: mock.MagicMock) -> None:
    can_access_google_page("https://www.google.com/webhp?client=firefox-b-d")
    mocked.assert_called_once()


@mock.patch("app.main.valid_google_url")
def test_have_valid_google_url(mocked: mock.MagicMock) -> None:
    can_access_google_page("https://www.google.com/webhp?client=firefox-b-d")
    mocked.assert_called_once_with(
        "https://www.google.com/webhp?client=firefox-b-d"
    )


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
def test_combination_of_returns(has_connect: bool,
                                valid_page: bool,
                                result: str) -> None:
    with (mock.patch("app.main.has_internet_connection") as mock_connect,
          mock.patch("app.main.valid_google_url") as mock_valid):
        mock_connect.return_value = has_connect
        mock_valid.return_value = valid_page
        link = "https://www.google.com/webhp?client=firefox-b-d"
        assert can_access_google_page(link) == result
