import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, valid_url, result_massage",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "should access to page when has internet connection and valid url.",
        "should`t access to page when has`t internet connection.",
        "should`t access to page when has`t valid url.",
        "should`t access to page when has`t internet connection and valid url."
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mock_valid_google_url: mock.MagicMock,
                                mock_has_internet_connection: mock.MagicMock,
                                internet_connection: bool,
                                valid_url: bool,
                                result_massage: str
                                ) -> None:

    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = internet_connection

    assert can_access_google_page("google.com") == result_massage
