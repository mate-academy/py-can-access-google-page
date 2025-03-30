from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize("correct_url, has_connection, expected", [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible")
]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_valid_google_url: mock.MagicMock,
                                mock_has_internet_connection: mock.MagicMock,
                                correct_url: bool,
                                has_connection: bool,
                                expected: str) -> None:
    mock_valid_google_url.return_value = correct_url
    mock_has_internet_connection.return_value = has_connection
    assert can_access_google_page("https://google.com/") == expected
