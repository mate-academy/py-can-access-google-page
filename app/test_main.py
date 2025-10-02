import datetime
import requests
from unittest import mock
import pytest
from typing import Any
from app.main import valid_google_url, has_internet_connection, can_access_google_page


def test_check_valid_url_and_internet_bool() -> None:
    assert isinstance(valid_google_url("https://www.google.com/"), bool)
    assert isinstance(has_internet_connection(), bool)


def test_can_access_google_page_str() -> None:
    assert isinstance(can_access_google_page("https://www.google.com/"), str)


@pytest.mark.parametrize(
    "internet, url, expected",
    [
        pytest.param(True, False, "Not accessible", id="(True, False)->Not accessible"),
        pytest.param(False, True, "Not accessible", id="(False, True)->Not accessible"),
        pytest.param(True, True, "Accessible", id="(True, True)->Accessible"),
    ]
)
def test_has_internet_connection(internet: bool, url: bool, expected: Any) -> None:
    with mock.patch("app.main.has_internet_connection", return_value=internet):
        with mock.patch("app.main.valid_google_url", return_value=url):
            assert can_access_google_page("https://www.google.com/") == expected


def test_has_internet_connection() -> None:
    good_time = datetime.datetime(2025, 1, 1, 22, 59, 59)
    fake_time = datetime.datetime(2025, 1, 1, 23, 0, 0)

    with mock.patch("datetime.datetime", return_value=fake_time) as mock_time:
        assert has_internet_connection() == False

    with mock.patch("datetime.datetime", return_value=good_time) as mock_time:
        assert has_internet_connection() == True