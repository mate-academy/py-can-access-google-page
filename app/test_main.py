import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url,is_internet_connection ,expected_result",
    [
        pytest.param(True, True, "Accessible", id="Page is accessible"),
        pytest.param(True,
                     False,
                     "Not accessible",
                     id="There is no internet connection"),
        pytest.param(False, True, "Not accessible", id="You have wrong url"),
        pytest.param(False,
                     False,
                     "Not accessible",
                     id="There is no internet connection and wrong url")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_valid_google_url: bool,
                                mocked_has_internet_connection: bool,
                                is_valid_url: bool,
                                is_internet_connection: bool,
                                expected_result: str):
    mocked_valid_google_url.return_value = is_valid_url
    mocked_has_internet_connection.return_value = is_internet_connection

    assert can_access_google_page("https://www.google.com") == expected_result
