import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet, valid_url, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "all_true",
        "no_internet",
        "invalid_url",
        "both_false",
    ],
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet: mock.Mock,
    mock_valid_url: mock.Mock,
    internet: bool,
    valid_url: bool,
    expected: str,
) -> None:
    mock_has_internet.return_value = internet
    mock_valid_url.return_value = valid_url

    result: str = can_access_google_page("https://google.com")

    assert result == expected
