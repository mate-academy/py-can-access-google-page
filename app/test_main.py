import pytest
from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,has_connection,expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_can_access: MagicMock,
        mocked_valid_url: MagicMock,
        valid_url: bool,
        has_connection: bool,
        expected_result: str
):
    mocked_valid_url.return_value = valid_url
    mocked_can_access.return_value = has_connection
    assert can_access_google_page("https://www.google.com") == expected_result



