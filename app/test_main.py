from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
    mocked_has_internet: mock.MagicMock,
    mocked_validator: mock.MagicMock,
) -> None:
    mocked_validator.return_value = True
    mocked_has_internet.return_value = True

    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_url_and_connection_exists(
    mocked_has_internet: mock.MagicMock,
    mocked_validator: mock.MagicMock,
) -> None:
    mocked_has_internet.return_value = True
    mocked_validator.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_no_connection(
    mocked_has_internet: mock.MagicMock,
    mocked_validator: mock.MagicMock,
) -> None:
    mocked_has_internet.return_value = False
    mocked_validator.return_value = True

    assert can_access_google_page("https://www.google.com") == "Not accessible"
