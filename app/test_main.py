from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_valid: bool,
                                mocked_internet: bool) -> None:
    mocked_internet.return_value = True
    mocked_valid.return_value = True

    assert can_access_google_page("https://stackoverflow.com/") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cannot_access_if_valid_false(mocked_valid: bool,
                                      mocked_internet: bool) -> None:
    mocked_internet.return_value = True
    mocked_valid.return_value = False

    assert can_access_google_page("https://stackoverflow") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cannot_access_if_internet_false(mocked_valid: bool,
                                         mocked_internet: bool) -> None:
    mocked_internet.return_value = False
    mocked_valid.return_value = True

    assert can_access_google_page("https://stackoverflow") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cannot_access_if_all_false(mocked_valid: bool,
                                    mocked_internet: bool) -> None:
    mocked_internet.return_value = False
    mocked_valid.return_value = False

    assert can_access_google_page("https://stackoverflow") == "Not accessible"
