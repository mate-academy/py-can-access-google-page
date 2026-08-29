from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_called(
        mocked_has_internet_connection: mock.Mock,
        mocked_valid_google_url: mock.Mock
) -> None:
    can_access_google_page("google.com")
    mocked_has_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once_with("google.com")


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_when_all_right(
        mocked_has_internet_connection: mock.Mock,
        mocked_valid_google_url: mock.Mock
) -> None:
    assert can_access_google_page("google.com") == "Accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_invalid_url(
        mocked_has_internet_connection: mock.Mock,
        mocked_valid_google_url: mock.Mock
) -> None:
    assert can_access_google_page("google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_no_internet_connection(
        mocked_has_internet_connection: mock.Mock,
        mocked_valid_google_url: mock.Mock
) -> None:
    assert can_access_google_page("google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_everything_wrong(
        mocked_has_internet_connection: mock.Mock,
        mocked_valid_google_url: mock.Mock
) -> None:
    assert can_access_google_page("google.com") == "Not accessible"
