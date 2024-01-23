import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url_return,has_internet_connection_return,result",
    [
        pytest.param(
            True,
            False,
            "Not accessible"
        ),
        pytest.param(
            False,
            True,
            "Not accessible"
        ),
        pytest.param(
            False,
            False,
            "Not accessible"
        ),
        pytest.param(
            True,
            True,
            "Accessible"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mock_internet_connection: mock.MagicMock,
        mock_google_url: mock.MagicMock,
        valid_google_url_return: bool,
        has_internet_connection_return: bool,
        result: str) -> None:
    mock_internet_connection.return_value = has_internet_connection_return
    mock_google_url.return_value = valid_google_url_return
    assert can_access_google_page("https://www.google.com") == result
