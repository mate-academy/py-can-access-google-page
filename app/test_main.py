from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_access: mock.MagicMock) -> None:
    mocked_access.return_value = False
    assert can_access_google_page("") == "Accessible"
