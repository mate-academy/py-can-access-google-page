import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, valid_url, result", [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible")
    ],
    ids=[
        "Can access page",
        "No internet connection",
        "URL is not valid"
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mock_connection: mock,
                                mock_url: mock,
                                internet_connection: bool,
                                valid_url: bool,
                                result: str) -> None:
    mock_connection.return_value = internet_connection
    mock_url.return_value = valid_url
    assert can_access_google_page("") == result
