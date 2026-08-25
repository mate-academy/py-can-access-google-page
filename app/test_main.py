from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_can_access_google_page_is_called(
        mockde_interned_access: str,
        mocked_valid_url: bool
) -> None:
    can_access_google_page(url="https://www.google.com")
    mockde_interned_access.assert_called_once()
    mocked_valid_url.assert_called()
