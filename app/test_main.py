from unittest import mock
import pytest
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, excepted_result",
    [
        pytest.param(
            True,
            True,
            "Accessible"
        ),
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
    ]
)
def test_can_access_google_page(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool,
        has_internet_connection: bool,
        valid_google_url: bool,
        excepted_result: str
) -> None:
    mock_has_internet_connection.return_value = has_internet_connection
    mock_valid_google_url.return_value = valid_google_url
    assert can_access_google_page("https://google.com") == excepted_result
