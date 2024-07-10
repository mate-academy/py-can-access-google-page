import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet, valid_url, expected", [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Should return accessible if correct url and has internet",
        "Should not return accessible if has no internet",
        "Should not return accessible if invalid url and has no internet",
        "Should not return accessible if invalid url and has no internet",
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet: bool,
        mock_valid_url: bool,
        has_internet: bool,
        valid_url: str,
        expected: str
) -> None:
    mock_has_internet.return_value = has_internet
    mock_valid_url.return_value = valid_url
    assert can_access_google_page("https://www.google.com") == expected
