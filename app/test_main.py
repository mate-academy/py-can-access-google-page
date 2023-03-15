from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_with_no_connection_no_valid_url(
        mocked_url: mock,
        mocked_connection: mock
) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = False

    assert can_access_google_page("https://www.udemy.com/") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_with_no_connection(
        mocked_url: mock,
        mocked_connection: mock
) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = False

    assert can_access_google_page("https://www.udemy.com/") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_with_no_valid_url(
        mocked_url: mock,
        mocked_connection: mock
) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = True

    assert can_access_google_page(
        "https://fiwww.udemy.com/"
    ) == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_accessible(mocked_url: mock, mocked_connection: mock) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = True

    assert can_access_google_page("https://www.udemy.com/") == "Accessible"
