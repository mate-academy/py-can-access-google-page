from unittest.mock import patch
from app.main import can_access_google_page
from freezegun import freeze_time


@freeze_time("2022-6-29 6:00:00")
@patch("app.main.valid_google_url")
def test_should_pass_if_time_is_6_00_00(mocked_valid_url):
    mocked_valid_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@freeze_time("2022-6-29 22:59:59")
@patch("app.main.valid_google_url")
def test_should_pass_if_time_is_22_59_59(mocked_valid_url):
    mocked_valid_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@freeze_time("2022-6-29 23:00:00")
@patch("app.main.valid_google_url")
def test_should_pass_if_time_is_23_00_0(mocked_valid_url):
    mocked_valid_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@freeze_time("2022-6-29 7:30:30")
@patch("app.main.valid_google_url")
def test_should_pass_if_response_is_200_and_time_is_7(mocked_valid_url):
    mocked_valid_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@freeze_time("2022-6-29 7:30:30")
@patch("app.main.valid_google_url")
def test_should_pass_if_response_is_not_200_and_time_is_7(mocked_valid_url):
    mocked_valid_url.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
