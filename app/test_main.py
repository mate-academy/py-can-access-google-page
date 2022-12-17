from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_be_accessible_with_valid_url_and_time(
    mocked_inet_connection: object,
    mocked_valid_google_url: object
) -> None:

    mocked_valid_google_url.return_value = True
    mocked_inet_connection.return_value = True

    assert (
        can_access_google_page("https://www.google.com/")
        == "Accessible"
    )


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_not_be_accessible_with_not_valid_url_and_valid_time(
    mocked_inet_connection: object,
    mocked_valid_google_url: object
) -> None:

    mocked_valid_google_url.return_value = False
    mocked_inet_connection.return_value = True

    assert (
        can_access_google_page("https://www.ggle.com/")
        == "Not accessible"
    )


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_not_be_accessible_with_valid_url_and_not_valid_time(
    mocked_inet_connection: object,
    mocked_valid_google_url: object
) -> None:

    mocked_valid_google_url.return_value = True
    mocked_inet_connection.return_value = False

    assert (
        can_access_google_page("https://www.google.com/")
        == "Not accessible"
    )


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_not_be_accessible_with_not_valid_url_and_time(
    mocked_inet_connection: object,
    mocked_valid_google_url: object
) -> None:

    mocked_valid_google_url.return_value = False
    mocked_inet_connection.return_value = False

    assert (
        can_access_google_page("https://www.ggle.com/")
        == "Not accessible"
    )
