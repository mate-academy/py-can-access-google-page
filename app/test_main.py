from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access(
        mocked_valid_url: mock,
        mocked_has_connection: mock
) -> None:
    mocked_valid_url.return_value = True
    mocked_has_connection.return_value = True
    assert can_access_google_page("some_url") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_cannot_access_if_only_has_connect(
        mocked_valid_url: mock,
        mocked_has_connection: mock
) -> None:
    mocked_valid_url.return_value = False
    mocked_has_connection.return_value = True
    assert can_access_google_page("some_url") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_cannot_connect_if_only_valid_url(
        mocked_valid_url: mock,
        mocked_has_connection: mock
) -> None:
    mocked_valid_url.return_value = True
    mocked_has_connection.return_value = False
    assert can_access_google_page("some_url") == "Not accessible"
