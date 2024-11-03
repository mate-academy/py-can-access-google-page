from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def mocked_has_internet():
    with mock.patch("app.main.has_internet_connection") as mock_test_internet:
        yield mock_test_internet


@pytest.fixture
def mocked_valid_url():
    with mock.patch("app.main.valid_google_url") as mock_test_valid_url:
        yield mock_test_valid_url


@pytest.mark.parametrize(
    "internet_status, url_status, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_valid_url_and_connection_exists(
        mocked_has_internet,
        mocked_valid_url,
        internet_status,
        url_status,
        expected_result
):
    mocked_has_internet.return_value = internet_status
    mocked_valid_url.return_value = url_status
    assert can_access_google_page("https://www.google.com") == expected_result
