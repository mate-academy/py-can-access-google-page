from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_return_accessible_when_all_func_true(
        mock_valid_google_url: any,
        mock_has_internet_connection: any
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    assert can_access_google_page(
        "http://www.google.com/intl/en/privacy"
    ) == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_return_not_accessible_when_internet_connection_false(
        mock_valid_google_url: any,
        mock_has_internet_connection: any
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    assert can_access_google_page(
        "http://www.google.com/intl/en/privacy"
    ) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_return_not_accessible_when_google_url_false(
        mock_valid_google_url: any,
        mock_has_internet_connection: any
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    assert can_access_google_page(
        "http://www.google.com/intl/en/privacy"
    ) == "Not accessible"
