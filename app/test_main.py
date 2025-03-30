import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize("is_online,is_valid_ulr,expected_result", [
    (True, True, "Accessible"),
    (False, False, "Not accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
])
def test_can_access_google_page(is_online: bool,
                                is_valid_ulr: bool,
                                expected_result: str) -> None:
    with (mock.patch("app.main.has_internet_connection")
          as mocked_has_connection,
          mock.patch("app.main.valid_google_url")
          as mocked_valid_url):
        mocked_has_connection.return_value = is_online
        mocked_valid_url.return_value = is_valid_ulr

        assert can_access_google_page(
            "http://google.com") == expected_result
