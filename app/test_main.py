import pytest
from app.main import can_access_google_page
from unittest import mock


@pytest.mark.parametrize(
    ("internet_connection", "valid_url", "expected_output"),
    [(True, True, "Accessible"),
     (False, False, "Not accessible"),
     (True, False, "Not accessible"),
     (False, True, "Not accessible"),
     ])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: mock.Mock,
        mock_has_internet_connection: mock.Mock,
        internet_connection: bool,
        valid_url: bool,
        expected_output: str) -> None:
    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = valid_url
    assert expected_output == can_access_google_page("http://www.google.com")
