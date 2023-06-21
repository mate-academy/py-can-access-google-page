from unittest import mock
import pytest

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "url,connection,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_accessibility_to_page(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock,
        url: bool,
        connection: bool,
        result: str
) -> None:
    mocked_valid_google_url.return_value = url
    mocked_has_internet_connection.return_value = connection

    assert can_access_google_page("a") == result
