from app.main import can_access_google_page
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "valid_google_url, has_internet, result_expected",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible")
    ])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet: None,
        mock_valid_google_url: None,
        valid_google_url: None,
        has_internet: None,
        result_expected: None
) -> None:
    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet.return_value = has_internet

    result = can_access_google_page("http://google.com")

    assert result == result_expected
