from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_is_not_valid(
        mocked_url: mock,
        mocked_connection: mock
) -> None:

    mocked_url.return_value = False
    mocked_connection.return_value = True

    assert can_access_google_page(
        "https://www.google.com.ua"
    ) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_connection_is_not_valid(
        mocked_url: mock,
        mocked_connection: mock
) -> None:

    mocked_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page(
        "https://www.google.com.ua"
    ) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_connection_and_url_are_valid(
        mocked_url: mock,
        mocked_connection: mock
) -> None:

    mocked_url.return_value = True
    mocked_connection.return_value = True

    assert can_access_google_page(
        "https://www.google.com.ua"
    ) == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_connection_and_url_are_not_valid(
        mocked_url: mock,
        mocked_connection: mock
) -> None:

    mocked_url.return_value = False
    mocked_connection.return_value = False

    assert can_access_google_page(
        "https:/w.google.com.ua"
    ) == "Not accessible"
