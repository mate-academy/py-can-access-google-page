from unittest import mock

import pytest

from .main import can_access_google_page


@pytest.mark.parametrize(
    "url,connection,result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_google_url_called(
        mock_url: bool,
        mock_connection: bool,
        url: bool,
        connection: bool,
        result: str
) -> None:
    mock_url.return_value = url
    mock_connection.return_value = connection
    assert can_access_google_page("https://www.google.com/") == result
