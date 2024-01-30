import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, expected_result",
    [
        pytest.param(True, True, "Accessible",
                     id="valid URL with internet connection"),
        pytest.param(True, False, "Not accessible",
                     id="valid URL without internet connection"),
        pytest.param(False, True, "Not accessible",
                     id="invalid URL with internet connection"),
        pytest.param(False, False, "Not accessible",
                     id="invalid URL without internet connection"),
    ]
)
def test_can_access_google_page(
    valid_url: bool,
    internet_connection: bool,
    expected_result: str
) -> None:
    with (
        patch("app.main.valid_google_url")
        as mock_valid_google_url,
        patch("app.main.has_internet_connection")
        as mock_has_internet_connection
    ):
        mock_valid_google_url.return_value = valid_url
        mock_has_internet_connection.return_value = internet_connection
        assert can_access_google_page("http://google.com") == expected_result
