import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    ("internet_result", "valid_url_result", "expected"),
    [
        pytest.param(True, True, "Accessible", id="url_and_internet_valid"),
        pytest.param(True, False, "Not accessible", id="internet_valid"),
        pytest.param(False, True, "Not accessible", id="url_valid"),
        pytest.param(False, False, "Not accessible", id="none_is_valid"),
    ],
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_returns_expected_result(
    mock_google_url: mock.Mock,
    mock_internet: mock.Mock,
    internet_result: bool,
    valid_url_result: bool,
    expected: str,
) -> None:
    mock_google_url.return_value = valid_url_result
    mock_internet.return_value = internet_result
    actual_result = can_access_google_page("https://google.com")
    assert actual_result == expected
