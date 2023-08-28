import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_valid, internet_connection, expected",

    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        url_valid: bool,
        internet_connection: bool,
        expected: str
) -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_valid_google_url,
          mock.patch("app.main.has_internet_connection")
          as mocked_has_internet_connection):

        mocked_valid_google_url.return_value = url_valid
        mocked_has_internet_connection.return_value = internet_connection

        assert can_access_google_page("https://google.com") == expected

        mocked_has_internet_connection.assert_called_once()
        if internet_connection:
            (mocked_valid_google_url.assert_called_once_with
             ("https://google.com"))
