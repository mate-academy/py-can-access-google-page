
from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.fixture(scope="module")
def url() -> str:
    return "https://www.google.com"


@pytest.mark.parametrize("internet_connection,"
                         "valid_url,"
                         "expected_output",
                         [
                             pytest.param(True, True, "Accessible",
                                          id="internet_available_success"),
                             pytest.param(False, True, "Not accessible",
                                          id="internet_unavailable_success"),
                             pytest.param(True, False, "Not accessible",
                                          id="internet_available_fail"),
                             pytest.param(False, False, "Not accessible",
                                          id="internet_unavailable_fail")
                         ])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet_connection: mock,
                                mock_valid_google_url: mock,
                                internet_connection: bool,
                                valid_url: bool,
                                expected_output: str,
                                url: str) -> None:
    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = valid_url
    assert can_access_google_page(url) == expected_output
