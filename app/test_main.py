import pytest
from unittest import mock


from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "url,is_valid,internet_connection,expected_status",
    [
        ("https://www.google.com", True, False, "Not accessible"),
        ("http:///a", False, True, "Not accessible"),
        ("https://mate.academy", True, False, "Not accessible"),

        ("https://www.youtube.com/watch?v=dQw4w9WgXcQ",
         True, True, "Accessible"),

        ("https://www.twitch.tv", True, True, "Accessible"),
        ("https://gidhub.com", False, False, "Not accessible")
    ],
    ids=[
        "should not be accessible when there's no internet connection",
        "should not be accessible when url is not valid",
        "should not be accessible when there's no internet connection",

        "should be accessible when url is valid "
        "and user has internet connection",

        "should be accessible when url is valid "
        "and user has internet connection",

        "should not be accessible when url is not valid "
        "and there's no internet connection"
    ]
)
def test_accesses_pages_correctly(mocked_valid_url: mock.Mock,
                                  mocked_has_internet_connection: mock.Mock,
                                  url: str,
                                  is_valid: bool,
                                  internet_connection: bool,
                                  expected_status: str) -> None:
    mocked_valid_url.return_value = is_valid
    mocked_has_internet_connection.return_value = internet_connection
    access_status = can_access_google_page(url)
    assert access_status == expected_status
