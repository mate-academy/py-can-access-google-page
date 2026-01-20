import pytest

from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "url, status, expected_str",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_acces_google_page(mock_url: mock,
                               mock_connection: mock,
                               url: bool,
                               status: bool,
                               expected_str: str) -> None:
    mock_url.return_value = url
    mock_connection.return_value = status
    assert can_access_google_page("https://www.google.com") == expected_str
