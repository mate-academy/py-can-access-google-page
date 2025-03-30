from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_when_url_is_correct_and_has_connection(
        mocked_valid_google_url: bool,
        mocked_internet_connection: bool
) -> None:
    mocked_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_when_url_is_incorrect(
        mocked_valid_google_url: bool,
        mocked_internet_connection: bool
) -> None:
    mocked_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False

    assert can_access_google_page(
        "https://glfbjixcvjle.com"
    ) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_when_time_less_6_and_more_23(
        mocked_valid_google_url: bool,
        mocked_internet_connection: bool
) -> None:
    mocked_internet_connection.return_value = False
    mocked_valid_google_url.return_value = True

    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_connection_and_incorrect_url(
        mocked_valid_google_url: bool,
        mocked_internet_connection: bool
) -> None:
    mocked_internet_connection.return_value = False
    mocked_valid_google_url.return_value = False

    assert can_access_google_page(
        "https://sldknlknvlksndlkvn.com"
    ) == "Not accessible"
