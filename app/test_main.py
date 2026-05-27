import pytest
from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_status, result_expected", [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid: MagicMock,
        mock_internet: MagicMock,
        valid_url: bool,
        internet_status: bool,
        result_expected: str
) -> None:
    mock_valid.return_value = valid_url
    mock_internet.return_value = internet_status

    assert can_access_google_page("https://google.com") == result_expected
    mock_valid.assert_called_once()
    mock_internet.assert_called_once()
