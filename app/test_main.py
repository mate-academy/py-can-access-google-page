import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, url_valid, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: mock.MagicMock,
        mock_valid_google_url: mock.MagicMock,
        internet_connection: bool,
        url_valid: bool,
        expected_result: str
) -> None:
    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = url_valid

    assert can_access_google_page("https://www.google.com") == expected_result
