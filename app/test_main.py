from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_response_ok, is_internet_connection, expected_result",
    [(True, False, "Not accessible"),
     (False, True, "Not accessible"),
     (False, False, "Not accessible"),
     (True, True, "Accessible")]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_valid_google_url: pytest.param,
        mock_has_internet: pytest.param,
        is_response_ok: bool,
        is_internet_connection: bool,
        expected_result: str
) -> None:
    mock_has_valid_google_url.return_value = is_response_ok
    mock_has_internet.return_value = is_internet_connection

    result = can_access_google_page("https://google.com")
    assert result == expected_result
