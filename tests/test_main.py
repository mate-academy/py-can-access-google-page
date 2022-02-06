from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_is_url_valid_and_has_connection(mocked_valid_google_url=True,
                                         mocked_has_internet_connection=True):
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_for_invalid_url_and_no_connection(mocked_valid_google_url,
                                           mocked_has_internet_connection):
    test_cases = [
        {
            "mocked_valid_google_url": False,
            "mocked_has_internet_connection": True
        },
        {
            "mocked_valid_google_url": False,
            "mocked_has_internet_connection": False
        },
        {
            "mocked_valid_google_url": True,
            "mocked_has_internet_connection": False
        }
    ]

    for test_case in test_cases:
        assert can_access_google_page("Not accessible")
