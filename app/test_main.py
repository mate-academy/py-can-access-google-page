import pytest
import unittest
from unittest import mock


from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "url,valid_google_url,has_internet_connection,can_access",
        [("https://www.youtube.com/watch?v=wbUgJHiaokY",
          True, True, "Accessible",),
         ("https://www.youtube.com/watch?v=wbUgJHiaokY",
          True, False, "Not accessible",),
         ("afsdfsf", False, True, "Not accessible",),
         ("fdsffsf", False, False, "Not accessible",)])
    def test_can_access_google_page(self, url: str, valid_google_url: bool,
                                    has_internet_connection: bool,
                                    can_access: str) -> None:
        with (mock.patch("app.main.valid_google_url") as mocked_url,
              mock.patch("app.main.has_internet_connection")
              as mocked_connection):
            mocked_url.return_value = valid_google_url
            mocked_connection.return_value = has_internet_connection
            assert can_access_google_page(url) == can_access


if __name__ == "__main__":
    unittest.main()
