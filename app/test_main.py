from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page(
        mock_valid_url: mock.Mock,
        mock_has_internet: mock.Mock
) -> None:
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_without_internet(
        mock_valid_url: mock.Mock,
        mock_has_internet: mock.Mock
) -> None:
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_can_access_google_page_with_invalid_url(
        mock_valid_url: mock.Mock,
        mock_has_internet: mock.Mock
) -> None:
    assert can_access_google_page("https://www.google.bad") == "Not accessible"
