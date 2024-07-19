import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, expected, valid_url, has_internet",
    [
        ("https://google.com", "Not accessible",
         True, False),
        ("https://www.google.com", "Accessible",
         True, True),
        ("https://www.gooawdawgle.com/search?q=hello",
         "Not accessible", False, True),
        ("https://www.adwawdaefr.com/search?q=hello",
         "Not accessible", False, False),
    ],
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: mock.Mock,
        mock_has_internet_connection: mock.Mock,
        url: str, expected: str, valid_url: bool,
        has_internet: bool) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_internet

    assert can_access_google_page(url) == expected
