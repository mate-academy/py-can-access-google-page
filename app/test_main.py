import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, has_internet, result_expected",
    [
        pytest.param(True, True, "Accessible", id="Full Access"),
        pytest.param(False, False, "Not accessible", id="Access denied"),
        pytest.param(False, True, "Not accessible", id="Invalid URL"),
        pytest.param(True, False, "Not accessible", id="No Internet access")
    ])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet: bool,
        mock_valid_google_url: bool,
        valid_google_url: bool,
        has_internet: bool,
        result_expected: str
) -> None:
    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet.return_value = has_internet

    result = can_access_google_page("http://google.com.ua")

    assert result == result_expected
