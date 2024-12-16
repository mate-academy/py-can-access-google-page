import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url_result,internet_connection_result,expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_has_internet_connection: MagicMock,
        mocked_valid_google_url: MagicMock,
        valid_url_result: bool,
        internet_connection_result: bool,
        expected: str
) -> None:
    mocked_valid_google_url.return_value = valid_url_result
    mocked_has_internet_connection.return_value = internet_connection_result

    assert can_access_google_page("url") == expected
