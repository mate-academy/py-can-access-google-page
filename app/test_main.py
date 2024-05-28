import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url_and_connection() -> tuple[mock.Mock, mock.Mock]:
    with (mock.patch("app.main.has_internet_connection")
          as mock_has_internet_connection,
          mock.patch("app.main.valid_google_url") as mock_valid_google_url):
        yield mock_has_internet_connection, mock_valid_google_url


@pytest.mark.parametrize(
    "is_valid_url,is_there_connection, expected_result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible")
    ],
    ids=[
        "valid url, there is connection",
        "incorrect url, there is not connection",
        "valid url, there is not connection",
        "invalid url, there is connection"
    ]
)
def test_can_access_google_page(
        mocked_valid_url_and_connection: tuple[mock.Mock, mock.Mock],
        is_valid_url: bool,
        is_there_connection: bool,
        expected_result: str
) -> None:

    mocked_url, mocked_connection = mocked_valid_url_and_connection
    mocked_url.return_value = is_valid_url
    mocked_connection.return_value = is_there_connection
    assert can_access_google_page("https://www.google.com") == expected_result
