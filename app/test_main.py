import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "test_link,test_connection,expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]

)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_connection(
        mock_valid_url: mock.MagicMock,
        mock_connection: mock.MagicMock,
        test_connection: bool,
        test_link: str,
        expected_result: str
) -> None:
    mock_valid_url.return_value = test_link
    mock_connection.return_value = test_connection
    assert can_access_google_page(mock_valid_url) == expected_result
