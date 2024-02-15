import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    ("url", "is_valid", "is_connected", "is_accessible"),
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://some-other-site.com", False, True, "Not accessible"),
        ("https://google.com", True, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_get_access_google_page(
        mocked_url: mock.MagicMock,
        mocked_connection: mock.MagicMock,
        url: str,
        is_valid: bool,
        is_connected: bool,
        is_accessible: str
) -> None:
    mocked_url.return_value = is_valid
    mocked_connection.return_value = is_connected
    assert can_access_google_page(url) == is_accessible
