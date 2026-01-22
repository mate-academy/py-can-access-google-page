from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_connection,is_valid_url,expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=["has_connection_valid_url",
         "no_connection_valid_url",
         "has_connection_invalid_url",
         "no_connection_invalid_url"]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mock_valid_google_url,
                                mock_has_internet_connection,
                                has_connection,
                                is_valid_url,
                                expected_result) -> None:
    mock_valid_google_url.return_value = is_valid_url
    mock_has_internet_connection.return_value = has_connection

    can_access_google_page("https://smfakeggl.net/")

    mock_has_internet_connection.assert_called_once()
    if mock_has_internet_connection.assert_called_once():
        mock_valid_google_url.assert_called_once_with("https://smfakeggl.net/")

    assert can_access_google_page("https://smfakeggl.net/") == expected_result
