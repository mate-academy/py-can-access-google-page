from typing import Callable
from unittest import mock


from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", create=True)
def test_can_access_google_page_url_validator(
        mocked_validator: Callable,
) -> None:
    url = "google"
    mocked_validator.return_value = False

    test_func = can_access_google_page(url)
    mocked_validator.assert_called_once_with(url)

    assert test_func == "Not accessible", (
        "Function should return `Not accessible` "
        "if url doesn't valid."
    )


@mock.patch("app.main.has_internet_connection", create=True)
def test_can_access_google_page_internet_connection(
        mock_internet_connection: Callable
) -> None:
    mock_internet_connection.return_value = False

    test_func = can_access_google_page("https://www.google.com/")
    mock_internet_connection.assert_called_once()

    assert test_func == "Not accessible", (
        "Function should return `Not accessible` "
        "If no connection."
    )
