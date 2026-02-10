from unittest import mock

import pytest
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize("valid_url,internet_connection,expected_result",
                         [
                             (True, False, "Not accessible"),
                             (False, True, "Not accessible"),
                             (True, True, "Accessible")
                         ])
def test_can_access_google_page(mocked_valid_google_url: mock.MagicMock,
                                mocked_has_internet_connection: mock.MagicMock,
                                valid_url: bool,
                                internet_connection: bool,
                                expected_result: str) -> None:
    mocked_valid_google_url.return_value = valid_url
    mocked_has_internet_connection.return_value = internet_connection
    assert can_access_google_page("google.com") == expected_result
