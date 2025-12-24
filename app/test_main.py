from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_all_func_is_accessible(valid_url: mock, has_internet: mock) -> None:
    has_internet.return_value = True
    valid_url.return_value = True

    assert can_access_google_page("google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_is_not_accessible(valid_url: mock,
                                     has_internet: mock) -> None:
    has_internet.return_value = True
    valid_url.return_value = False

    assert can_access_google_page("google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_has_internet_is_not_accessible(valid_url: mock,
                                        has_internet: mock) -> None:
    valid_url.return_value = True
    has_internet.return_value = False

    assert can_access_google_page("google.com") == "Not accessible"
