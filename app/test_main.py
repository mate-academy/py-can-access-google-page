from unittest import mock


from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page_with_valid_url_and_time(
        mocked_url: bool,
        mocked_internet_connection: bool
) -> None:

    mocked_url.return_value = True
    mocked_internet_connection.return_value = True
    assert can_access_google_page("google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page_with_not_valid_url_and_time(
        mocked_url: bool,
        mocked_internet_connection: bool
) -> None:

    mocked_url.return_value = False
    mocked_internet_connection.return_value = False
    assert can_access_google_page("google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page_with_valid_url_and_not_valid_time(
        mocked_url: bool,
        mocked_internet_connection: bool
) -> None:

    mocked_url.return_value = True
    mocked_internet_connection.return_value = False
    assert can_access_google_page("google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page_with_not_valid_url_and_valid_time(
        mocked_url: bool,
        mocked_internet_connection: bool
) -> None:

    mocked_url.return_value = False
    mocked_internet_connection.return_value = True
    assert can_access_google_page("google.com") == "Not accessible"
