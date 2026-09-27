import pytest
from unittest.mock import MagicMock, patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_value, internet_value, result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_url: MagicMock,
    mock_internet: MagicMock,
    url_value: bool,
    internet_value: bool,
    result: str
) -> None:
    mock_url.return_value = url_value
    mock_internet.return_value = internet_value
    assert (
        can_access_google_page("https://www.google.com") == result
    ), f"Expected {result} when url: {url_value} & internet: {internet_value}"
