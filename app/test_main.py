from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url,has_internet,excepted_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet: MagicMock,
        mock_valid_google_url: MagicMock,
        is_valid_url: bool,
        has_internet: bool,
        excepted_result: str) -> None:
    mock_valid_google_url.return_value = is_valid_url
    mock_has_internet.return_value = has_internet
    assert can_access_google_page("https://www.google.com") == excepted_result
