from unittest.mock import patch, Mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet,valid_google_url,expected",
    [
        pytest.param(
            True, True, "Accessible",
            id="If you have valid URL and internet connection, "
               "return 'Accessible'"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="If you don't have valid URL, return 'Not accessible'"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="If you don't have internet connection, "
               "return 'Not accessible'"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="If you haven't valid URL and don't have internet connection, "
               "return 'Not accessible'"
        )
    ],

)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock,
        has_internet: bool,
        valid_google_url: bool,
        expected: str
) -> None:
    mock_has_internet_connection.return_value = has_internet
    mock_valid_google_url.return_value = valid_google_url
    assert can_access_google_page("www.google.com") == expected
