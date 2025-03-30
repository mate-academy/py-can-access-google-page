from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google(
        mock_valid_google_url: mock.MagicMock,
        mock_internet: mock.MagicMock,
        valid_url: bool,
        internet: bool,
        expected_result: bool
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_internet.return_value = internet
    assert can_access_google_page("www.some_url.ua") == expected_result
