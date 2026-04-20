import pytest
from unittest import mock
from unittest.mock import MagicMock

from .main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "mock_valid_google_url_value, mock_has_internet_connection_value, result",
    [
        pytest.param(True, True, "Accessible", id="both functions are valid"),
        pytest.param(True, False, "Not accessible", id="without internet connection"),
        pytest.param(False, True, "Not accessible", id="with incorrect url"),
        pytest.param(False, False, "Not accessible", id="with incorrect url and without internet connection"),
    ]
)
def test_can_access_google_page_with_different_states(
    mock_has_internet_connection: MagicMock,
    mock_valid_google_url: MagicMock,
    mock_valid_google_url_value: bool,
    mock_has_internet_connection_value: bool,
    result: str
) -> None:
    mock_valid_google_url.return_value = mock_valid_google_url_value
    mock_has_internet_connection.return_value = mock_has_internet_connection_value

    assert can_access_google_page("https://www.google.com") == result