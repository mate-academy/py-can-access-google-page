import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, connection, expected",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_url: mock,
                                mock_connection: mock,
                                url: bool,
                                connection: bool,
                                expected: str) -> None:
    mock_url.return_value = url
    mock_connection.return_value = connection
    assert can_access_google_page("url") == expected
