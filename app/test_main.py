import pytest
from unittest import mock
from app.main import can_access_google_page



@pytest.mark.parametrize(
    "initial_url, initial_internet, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)

@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_internet, mocked_url, initial_url, initial_internet, expected_result):
    mocked_url.return_value = initial_url
    mocked_internet.return_value = initial_internet
    assert can_access_google_page("https://www.google.com") == expected_result
