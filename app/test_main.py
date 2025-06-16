import pytest
from unittest import mock
from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize("connection, valid_url, expected", [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ])
    def test_can_access_google_page(
            self, connection: bool, valid_url: bool, expected: str
    ) -> None:
        with mock.patch("app.main.has_internet_connection",
                        return_value=connection), \
             mock.patch("app.main.valid_google_url", return_value=valid_url):
            res = can_access_google_page("https://www.google.com/")
            assert res == expected
