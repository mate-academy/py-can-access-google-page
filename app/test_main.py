import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, internet_connection, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")

def test_can_acces_google_page(mocked_url: mock,
                               mock_connection: mock,
                               url: bool, 
                               internet_connection: bool,
                               expected_result: str) -> None:
    mocked_url.return_value = url
    mock_connection.return_value = internet_connection
    assert can_access_google_page("https://www.google.com/") == expected_result
