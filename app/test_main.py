import pytest


from unittest import mock


from app.main import can_access_google_page


VALID_URL = "https://www.youtube.com/"
INVALID_URL = "https:/ww.you1t1u1be.com/"


@pytest.mark.parametrize(
    "has_internet_connection, is_valid_url, url, expected",
    [
        pytest.param(
            True, True, VALID_URL, "Accessible"
        ),
        pytest.param(
            False, True, VALID_URL, "Not accessible"
        ),
        pytest.param(
            True, False, INVALID_URL, "Not accessible"
        ),
        pytest.param(
            False, False, INVALID_URL, "Not accessible"
        ),
    ],
    ids=[
        "You should be able to enter website if url is correct"
        " and you have internet connection",
        "You shouldn't be able to enter website if url is correct"
        " and you don't have internet connection",
        "You shouldn't be able to enter website if url is incorrect"
        " and you have internet connection",
        "You shouldn't be able to enter website if url is incorrect"
        " and you don't have internet connection",
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
    mocked_connection: mock.Mock,
    mocked_valid: mock.Mock,
    has_internet_connection: bool,
    is_valid_url: bool,
    url: str,
    expected: str,
) -> None:
    mocked_connection.return_value = has_internet_connection
    mocked_valid.return_value = is_valid_url
    assert can_access_google_page(url) == expected
