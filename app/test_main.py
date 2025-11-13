import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet,url_valid,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "Has connection and correct url",
        "Has connection but incorrect url",
        "Dont has connection and correct url",
        "DOnt has connection and incorrect url"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_valid_url: mock.MagicMock,
    mock_has_internet: mock.MagicMock,
    internet: bool,
    url_valid: bool,
    expected: str
) -> None:
    mock_has_internet.return_value = internet
    mock_valid_url.return_value = url_valid

    result = can_access_google_page("https://www.google.com/")
    assert result == expected
