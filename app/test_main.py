import pytest
from unittest.mock import patch
from app.main import (valid_google_url,
                  has_internet_connection,
                  can_access_google_page)
from unittest import mock


@pytest.mark.parametrize(
        "valid_url, internet_connection, expected_result",
        [
            (True, True, "Accessible"),
            (False, True, "Not accessible"),
            (False, False, "Not accessible"),
            (True, False, "Not accessible"),
        ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mocked_internet_connection: mock,
                                mocked_valid: mock,
                                valid_url: bool,
                                internet_connection: bool,
                                expected_result: str) -> None:
    mocked_internet_connection.return_value = internet_connection
    mocked_valid.return_value = valid_url
    assert can_access_google_page("https://www.google.com/") == expected_result
