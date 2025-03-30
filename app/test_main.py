import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection,url,result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible"),
        (True, True, "Accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_cannot_access_if_only_connection(
        mocked_connection: mock,
        mocked_url: mock,
        connection: bool,
        url: bool,
        result: str
) -> None:
    mocked_connection.return_value = connection
    mocked_url.return_value = url

    assert can_access_google_page("https://www.google.com") == result
