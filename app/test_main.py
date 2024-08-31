from unittest import mock

from app.main import can_access_google_page


url = "https://www.google.com"


@mock.patch("app.main.valid_google_url")
def test_if_function_receives_wrong_url(false_google_url: object) -> None:
    false_google_url.return_value = False
    assert can_access_google_page(url) == "Not accessible"


@mock.patch("app.main.has_internet_connection")
def test_no_internet_access(has_no_internet: object) -> None:
    has_no_internet.return_value = False
    assert can_access_google_page(url) == "Not accessible"


def test_all_true() -> None:
    with mock.patch("app.main.has_internet_connection") as internet_true:
        internet_true.return_value = True
        with mock.patch("app.main.valid_google_url") as url_true:
            url_true.return_value = True
            assert can_access_google_page(url) == "Accessible"


def test_all_false() -> None:
    with mock.patch("app.main.has_internet_connection") as internet_false:
        internet_false.return_value = False
        with mock.patch("app.main.valid_google_url") as url_false:
            url_false.return_value = False
            assert can_access_google_page(url) == "Not accessible"
