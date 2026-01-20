import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, hour_access, response",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_url: mock,
        mock_valid_time: mock,
        url: bool,
        hour_access: bool,
        response: str,

) -> None:
    mock_valid_url.return_value = url
    mock_valid_time.return_value = hour_access
    assert can_access_google_page("link_start_google_page") == response
