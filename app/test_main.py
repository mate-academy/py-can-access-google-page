from unittest import mock
import pytest

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "url,connection,expected_result",
    [
        pytest.param(True, True, "Accessible", id=""),
        pytest.param(True, False, "Not accessible", id=""),
        pytest.param(False, True, "Not accessible", id=""),
        pytest.param(False, False, "Not accessible", id="")
    ]
)
def test_accessibility_to_page(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock,
        url: bool,
        connection: bool,
        expected_result: str
) -> None:
    mocked_valid_google_url.return_value = url

    mocked_has_internet_connection.return_value = connection

    assert can_access_google_page(" ") == expected_result
