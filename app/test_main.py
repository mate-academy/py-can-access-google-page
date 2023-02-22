from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection_status,url_status,expected",
    [
        pytest.param(
            True, True, "Accessible",
            id="accessible when ok connection, ok url"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="not accessible when ok connection, bad url"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="not accessible when no connection, ok url"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_ok_connection_ok_url(
    mock_connection: mock,
    mock_url: mock,
    connection_status: bool,
    url_status: bool,
    expected: str
) -> None:
    mock_connection.return_value = connection_status
    mock_url.return_value = url_status
    assert can_access_google_page("google.com") == expected
