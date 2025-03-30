from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,has_connection,access",
    [
        pytest.param(
            True, True, "Accessible",
            id="Returns 'Accessible' when have valid url and have connection"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="Returns 'Not accessible' when have valid url but no connection"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="Returns 'Not accessible' when have connection but invalid url"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="Returns 'Not accessible' if have invalid url and no connection"
        )
    ]
)
def test_can_access_google_page(
        valid_url: bool,
        has_connection: bool,
        access: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mock_valid_google_url,
        mock.patch("app.main.has_internet_connection") as mock_has_connection
    ):
        mock_valid_google_url.return_value = valid_url
        mock_has_connection.return_value = has_connection
        assert can_access_google_page("https://www.google.com.ua") == access
