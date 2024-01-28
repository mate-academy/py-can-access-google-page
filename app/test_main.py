from app.main import can_access_google_page
from unittest import mock
import datetime


def test_check_correct_url() -> None:
    assert (
        can_access_google_page("https://www.google.com/") == "Accessible"
    )


def test_check_wrong_url() -> None:
    assert (
        can_access_google_page("https://www.amazon.com/") == "Not accessible"
    )


@mock.patch("app.main.datetime.datetime")
def test_url_func_execution(valid: mock) -> None:
    valid.return_value = (datetime.datetime.now()).replace(hour=5, minute=0)
    assert (
        can_access_google_page("https://www.google.com") == "Not accessible"
    )


@mock.patch("app.main.can_access_google_page")
def test_access_func_execution(access: mock) -> None:
    access.return_value = False
    assert (
        can_access_google_page("https://www.google.com") == "Accessible"
    )
