from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_with_true_true(
        mock_connection: mock.MagicMock,
        mock_valid: mock.MagicMock
) -> None:
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_with_false_true(
        mock_connection: mock.MagicMock,
        mock_valid: mock.MagicMock
) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_with_true_false(
        mock_connection: mock.MagicMock,
        mock_valid: mock.MagicMock
) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"
