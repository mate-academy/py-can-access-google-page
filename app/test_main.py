import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "allowed_url, allowed_time, result",
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
        mock_valid_url: mock.MagicMock,
        mock_internet_connection: mock.MagicMock,
        allowed_time: bool,
        allowed_url: bool,
        result: str
) -> None:
    mock_valid_url.return_value = allowed_url
    mock_internet_connection.return_value = allowed_time
    assert can_access_google_page("www.google.com") == result
