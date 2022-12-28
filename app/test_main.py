from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_give_access_if_has_internet_connection_and_valid_url(
        mocked_connection: mock,
        mocked_url: mock
) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page(mocked_url) == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_not_give_access_if_has_not_internet_connection(
        mocked_connection: mock,
        mocked_url: mock
) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page(mocked_url) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_not_give_access_if_url_is_not_valid(
        mocked_connection: mock,
        mocked_url: mock
) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page(mocked_url) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_not_give_access_if_url_and_internet_connection_is_false(
        mocked_connection: mock,
        mocked_url: mock
) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = False
    assert can_access_google_page(mocked_url) == "Not accessible"
