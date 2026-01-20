from unittest import mock
from unittest.mock import MagicMock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,is_valid_url,has_internet_connection,expected",
    [
        pytest.param(
            "https://www.google.com",
            True,
            True,
            "Accessible",
            id="all conditions True",
        ),
        pytest.param(
            "https://www.google.com",
            False,
            True,
            "Not accessible",
            id="invalid google url",
        ),
        pytest.param(
            "https://www.google.com",
            True,
            False,
            "Not accessible",
            id="no internet connection",
        ),
        pytest.param(
            "https://www.google.com",
            False,
            False,
            "Not accessible",
            id="all conditions False",
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock,
        url: str,
        is_valid_url: bool,
        has_internet_connection: bool,
        expected: str
) -> None:
    mock_valid_google_url.return_value = is_valid_url
    mock_has_internet_connection.return_value = has_internet_connection
    assert can_access_google_page(url) == expected
