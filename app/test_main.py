import pytest


from unittest import mock


from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, valid_url, url, expected",
    [
        pytest.param(
            True, True, "https://www.youtube.com/", "Accessible"
        ),
        pytest.param(
            False, True, "https://www.youtube.com/", "Not accessible"
        ),
        pytest.param(
            True, False, "https:/ww.you1t1u1be.com/", "Not accessible"
        ),
        pytest.param(
            False, False, "https:/ww.you1t1u1be.com/", "Not accessible"
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
    internet_connection: bool,
    valid_url: bool,
    url: str,
    expected: str,
) -> None:
    mocked_connection.return_value = internet_connection
    mocked_valid.return_value = valid_url
    assert can_access_google_page(url) == expected
