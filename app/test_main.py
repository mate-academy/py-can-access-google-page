from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_accessible(
        mock_valid_google_url: str,
        mock_has_internet_connection: bool
) -> None:
    assert can_access_google_page(mock_valid_google_url)
