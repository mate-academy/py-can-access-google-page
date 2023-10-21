from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "test_url,result",
    [
        ("https://www.google.com/", "Accessible"),
        ("htpp://www.goole.com/", "Not accessible")
    ]
)
def test_valid_url_and_connection_exists(test_url: str, result: str) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mocked_valid_google_url,
        mock.patch("app.main.has_internet_connection")
        as mocked_has_internet_connection
    ):

        can_access_google_page(test_url)
        mocked_valid_google_url.assert_called_with(test_url)
        mocked_has_internet_connection.assert_called()
