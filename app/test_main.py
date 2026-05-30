from unittest.mock import Mock, patch

from app import main


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_should_return_accessible_when_url_is_valid_and_internet_exists(
    mock_has_internet_connection: Mock,
    mock_valid_google_url: Mock,
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True

    assert (
        main.can_access_google_page("https://google.com")
        == "Accessible"
    )


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_should_return_not_accessible_when_only_internet_exists(
    mock_has_internet_connection: Mock,
    mock_valid_google_url: Mock,
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False

    assert (
        main.can_access_google_page("https://google.com")
        == "Not accessible"
    )


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_should_return_not_accessible_when_only_url_is_valid(
    mock_has_internet_connection: Mock,
    mock_valid_google_url: Mock,
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True

    assert (
        main.can_access_google_page("https://google.com")
        == "Not accessible"
    )


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_should_return_not_accessible_when_no_internet_and_invalid_url(
    mock_has_internet_connection: Mock,
    mock_valid_google_url: Mock,
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False

    assert (
        main.can_access_google_page("https://google.com")
        == "Not accessible"
    )
