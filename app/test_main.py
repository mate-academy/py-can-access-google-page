from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_accessible_when_url_valid_and_connection_exists(
        mocked_valid_url: mock.MagicMock,
        mocked_connection: mock.MagicMock
) -> None:
    mocked_valid_url.return_value = True
    mocked_connection.return_value = True

    assert can_access_google_page("https://www.google.com/") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_when_url_valid_but_no_connection(
        mocked_valid_url: mock.MagicMock,
        mocked_connection: mock.MagicMock
) -> None:
    mocked_valid_url.return_value = True
    mocked_connection.return_value = False

    assert (
        can_access_google_page("https://www.google.com/") == "Not accessible"
    )


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_when_connection_exists_but_url_invalid(
        mocked_valid_url: mock.MagicMock,
        mocked_connection: mock.MagicMock
) -> None:
    mocked_valid_url.return_value = False
    mocked_connection.return_value = True

    assert (
        can_access_google_page("https://www.google.com/") == "Not accessible"
    )


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_when_url_invalid_and_no_connection(
        mocked_valid_url: mock.MagicMock,
        mocked_connection: mock.MagicMock
) -> None:
    mocked_valid_url.return_value = False
    mocked_connection.return_value = False

    assert (
        can_access_google_page("https://www.google.com/") == "Not accessible"
    )
