import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url_return, has_internet_connection_return, result",
    [
        pytest.param(True, False, "Not accessible"),
        pytest.param(False, True, "Not accessible"),
        pytest.param(False, False, "Not accessible"),
        pytest.param(True, True, "Accessible")
    ],
    ids=[
        "Only has_internet_connection Fail",
        "Only valid_google_url Fail",
        "Both are Fail",
        "Both are True"
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock,
        valid_google_url_return: bool,
        has_internet_connection_return: bool,
        result: str,

) -> None:
    mock_valid_google_url.return_value = valid_google_url_return
    mock_has_internet_connection.return_value = has_internet_connection_return

    assert can_access_google_page("url") == result
