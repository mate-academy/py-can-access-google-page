import pytest
from app.main import can_access_google_page


def test_can_access_google_page(mocker) -> None:
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=True)

    assert can_access_google_page("https://google.com") == "Accessible"


def test_can_not_access_if_not_valid_url(mocker) -> None:
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=True)

    assert can_access_google_page("https://google.com") == "Not accessible"


def test_can_not_access_if_not_internet_connection(mocker) -> None:
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=False)

    assert can_access_google_page("https://google.com") == "Not accessible"

def test_can_not_access_if_both_not_true(mocker) -> None:
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=False)

    assert can_access_google_page("https://google.com") == "Not accessible"
