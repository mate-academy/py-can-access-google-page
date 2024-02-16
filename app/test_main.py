import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,connection,access",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Valid url is True, Internet connection is True",
        "Valid url is True, Internet connection is False",
        "Valid url is False, Internet connection is True",
        "Valid url is False, Internet connection is False",
    ]
)
def test_can_access_google_page(
        valid_url: bool,
        connection: bool,
        access: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mock_valid_google_url,
        mock.patch("app.main.has_internet_connection") as mock_has_connection
    ):
        mock_valid_google_url.return_value = valid_url
        mock_has_connection.return_value = connection
        assert can_access_google_page("google") == access
