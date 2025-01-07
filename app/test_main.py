import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,valid_url,connection,access",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://google.com", True, False, "Not accessible"),
        ("https://google.com", False, True, "Not accessible"),
        ("https://google.com", False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_valid_url: mock.MagicMock,
                                mocked_internet_connection: mock.MagicMock,
                                url: str,
                                valid_url: bool,
                                connection: bool,
                                access: str) -> None:
    mocked_valid_url.return_value = valid_url
    mocked_internet_connection.return_value = connection

    assert can_access_google_page(url) == access
