import pytest
from unittest import mock
from app import main


@pytest.mark.parametrize(
    "url, internet, valid_url, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("http://www.goole.com", True, False, "Not accessible"),
        ("https://www.google.com", False, True, "Not accessible"),
        ("http://www.goole.com", False, False, "Not accessible"),
    ],
)
def test_can_access_google_page_scenarios(
    url: str,
    internet: bool,
    valid_url: bool,
    expected: str,
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mock_valid_url,
        mock.patch("app.main.has_internet_connection") as mock_internet_connection,
    ):
        mock_valid_url.return_value = valid_url
        mock_internet_connection.return_value = internet

        result = main.can_access_google_page(url)

        assert result == expected
        mock_internet_connection.assert_called_once()

        # важно из-за short-circuit
        if internet:
            mock_valid_url.assert_called_once_with(url)
        else:
            mock_valid_url.assert_not_called()
