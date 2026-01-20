from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "return_val_for_valid_url, return_val_for_internet_conn, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page_check_return_values(
        mock_valid_url: mock.MagicMock,
        mock_has_internet: mock.MagicMock,
        return_val_for_valid_url: bool,
        return_val_for_internet_conn: bool,
        expected_result: str
) -> None:

    mock_valid_url.return_value = return_val_for_valid_url
    mock_has_internet.return_value = return_val_for_internet_conn
    assert can_access_google_page("https://www.google.com/") == expected_result
