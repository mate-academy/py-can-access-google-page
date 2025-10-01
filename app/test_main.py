import pytest
from app.main import can_access_google_page


def test_accessible_when_both_conditions_true(mocker):
    mocker.patch("app.main.has_internet_connection", return_value=True)
    mocker.patch("app.main.valid_google_url", return_value=True)

    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


def test_not_accessible_when_no_internet(mocker):
    mocker.patch("app.main.has_internet_connection", return_value=False)
    mocker.patch("app.main.valid_google_url", return_value=True)

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


def test_not_accessible_when_invalid_url(mocker):
    mocker.patch("app.main.has_internet_connection", return_value=True)
    mocker.patch("app.main.valid_google_url", return_value=False)

    result = can_access_google_page("https://fake-url.com")
    assert result == "Not accessible"


def test_not_accessible_when_both_conditions_false(mocker):
    mocker.patch("app.main.has_internet_connection", return_value=False)
    mocker.patch("app.main.valid_google_url", return_value=False)

    result = can_access_google_page("https://fake-url.com")
    assert result == "Not accessible"
