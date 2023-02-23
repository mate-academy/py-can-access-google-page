from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, connection, access",
    [
        pytest.param(True, True, "Accessible",
                     id="Test can access. All valid"),
        pytest.param(True, False, "Not accessible",
                     id="Test can access. Only has connection"),
        pytest.param(False, True, "Not accessible",
                     id="Test can access. Only valid url"),
        pytest.param(False, False, "Not accessible",
                     id="Test can access. Not connect, not valid"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid: mock,
        mocked_connection: mock,
        valid_url: bool,
        connection: bool,
        access: str
) -> None:
    mocked_valid.return_value = valid_url
    mocked_connection.return_value = connection
    assert can_access_google_page("https://www.google.com.ua/") == access
