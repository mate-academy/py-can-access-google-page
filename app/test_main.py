from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page_with_true_false(
        mock_valid_url: bool,
        mock_connection: bool
) -> None:

    mock_valid_url.return_value = True
    mock_connection.return_value = False

    assert can_access_google_page("") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page_with_false_true(
        mock_valid_url: bool,
        mock_connection: bool
) -> None:

    mock_valid_url.return_value = False
    mock_connection.return_value = True

    assert can_access_google_page("") == "Not accessible"
