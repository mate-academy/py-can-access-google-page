import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_internet, result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_access_to_google(
        mock_has_internet_connection: mock,
        mock_valid_google_url: mock,
        valid_url: bool,
        has_internet: bool,
        result: str
) -> None:
    mock_has_internet_connection.return_value = has_internet
    mock_valid_google_url.return_value = valid_url
    assert can_access_google_page("google.com") == result
