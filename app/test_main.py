import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,has_internet,result",
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
        valid_url: bool,
        has_internet: bool,
        result: str
) -> None:
    mock_has_internet_connection.return_value = has_internet
    mock_valid_google_url = valid_url
    assert can_access_google_page("http://www.google.com") == result
