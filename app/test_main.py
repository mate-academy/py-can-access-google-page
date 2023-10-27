import pytest
from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "url, connect, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_access_google_page(
        mock_url: mock,
        mock_connect: mock,
        url: bool,
        connect: bool,
        result: str
) -> None:
    mock_url.return_value = url
    mock_connect.return_value = connect
    assert can_access_google_page("https/:google.com") == result
