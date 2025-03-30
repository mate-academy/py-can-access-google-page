import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Accessible with internet and valid URL",
        "Not accessible: has internet, but invalid URL",
        "Not accessible: valid URL, but no internet",
        "Not accessible: no internet, invalid URL",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet: bool,
        mock_is_valid_url: bool,
        internet_connection: bool,
        valid_url: bool,
        expected: str,
) -> None:
    mock_has_internet.return_value = internet_connection
    mock_is_valid_url.return_value = valid_url
    assert can_access_google_page("http://google.com") == expected
