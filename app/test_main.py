import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, connection, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
class TestClass():
    def test_can_access_google_page(self,
                                    url: bool,
                                    connection: bool,
                                    expected: str) -> None:
        test_url = "https://example.com"
        with (
            mock.patch("app.main.valid_google_url") as valid_url,
            mock.patch("app.main.has_internet_connection") as has_connection
        ):
            valid_url.return_value = url
            has_connection.return_value = connection

            result = can_access_google_page(test_url)

            has_connection.assert_called_once()
            if connection:
                valid_url.assert_called_once_with(test_url)

            assert result == expected
