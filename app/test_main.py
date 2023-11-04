import pytest
from unittest import mock


from .main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url,has_internet_connection",
    [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mocked_valid_google_url: mock,
    mocked_has_internet_connection: mock,
    valid_google_url: bool,
    has_internet_connection: bool
) -> None:
    print(mocked_valid_google_url, mocked_has_internet_connection)
    print(valid_google_url, has_internet_connection)
    url = "https://www.google.com"
    mocked_valid_google_url.return_value = valid_google_url
    mocked_has_internet_connection.return_value = has_internet_connection

    if valid_google_url and has_internet_connection:
        assert can_access_google_page(url) == "Accessible"
    else:
        assert can_access_google_page(url) == "Not accessible"
