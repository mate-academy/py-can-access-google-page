from unittest.mock import MagicMock

import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "test_can_access_google_page",
        "test_cannot_access_if_only_connection",
        "test_cannot_access_if_only_valid_url",
        "test_cannot_access_if_connection_and_valid_false"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_internet: MagicMock,
        mock_valid_url: MagicMock,
        internet: bool,
        valid_url: bool,
        expected: str
) -> None:
    mock_internet.return_value = internet
    mock_valid_url.return_value = valid_url

    assert can_access_google_page("https://www.google.com") == expected
    mock_internet.assert_called_once()
    if internet:
        mock_valid_url.assert_called_once_with("https://www.google.com")
    else:
        mock_valid_url.assert_not_called()
