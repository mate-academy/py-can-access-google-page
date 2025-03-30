import pytest
from unittest import mock


from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, has_internet, valid_url, result",
    [
        ("https://www.google.com/", True, True, "Accessible"),
        ("https://www.google.com/", False, True, "Not accessible"),
        ("https/ww.googl/e.,com", True, False, "Not accessible"),
        ("https/ww.googl/e.,com", False, False, "Not accessible"),
    ],
    ids=[
        "Test - has internet and valid url",
        "Test - without internet and with valid url",
        "Test - has internet and invalid url",
        "Test - without internet and with invalid url"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_url: callable,
                                mocked_internet: callable,
                                url: str,
                                has_internet: bool,
                                valid_url: bool,
                                result: str) -> None:
    mocked_url.return_value = valid_url
    mocked_internet.return_value = has_internet
    assert can_access_google_page(url) == result
