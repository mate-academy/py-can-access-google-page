import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_link, valid_connection, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_url: mock.Mock,
                                mocked_connection: mock.Mock,
                                valid_link: bool,
                                valid_connection: bool,
                                result: str
                                ) -> None:
    mocked_url.return_value = valid_link
    mocked_connection.return_value = valid_connection
    assert (can_access_google_page("https://www.google.com")
            == result)
