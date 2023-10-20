import pytest
from app.main import can_access_google_page
from unittest import mock


@pytest.mark.parametrize(
    "url_return, connection_return, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_url: mock,
                                mock_connection: mock,
                                url_return: bool,
                                connection_return: bool,
                                expected_result: str) -> None:
    mock_url.return_value = url_return
    mock_connection.return_value = connection_return
    assert can_access_google_page("url") == expected_result
