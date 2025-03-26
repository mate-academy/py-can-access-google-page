from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_valid_url, mock_has_internet, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(mock_valid_url: bool,
                                mock_has_internet: bool,
                                expected: str) -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        with mock.patch("app.main.valid_google_url") as mocked_valid:
            mocked_connection.return_value = mock_valid_url
            mocked_valid.return_value = mock_has_internet
            assert can_access_google_page("https://www.google.com") == expected
