import pytest
from unittest import mock
from unittest.mock import MagicMock

from .main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "url_status, internet_status, result",
    [
        pytest.param(
            True, True, "Accessible",
            id="both functions are valid"),
        pytest.param(
            True, False, "Not accessible",
            id="without internet connection"),
        pytest.param(
            False, True, "Not accessible",
            id="with incorrect url"),
        pytest.param(
            False, False, "Not accessible",
            id="with incorrect url and without internet connection"),
    ]
)
def test_can_access_google_page_with_different_states(
    mock_has_internet_connection: MagicMock,
    mock_valid_google_url: MagicMock,
    url_status: bool,
    internet_status: bool,
    result: str
) -> None:
    mock_valid_google_url.return_value = url_status
    mock_has_internet_connection.return_value = internet_status

    assert can_access_google_page("https://www.google.com") == result
