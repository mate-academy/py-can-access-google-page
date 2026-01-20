import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
    ],
)
def test_can_access_google_page(
    valid_google_url: bool, has_internet_connection: bool, result: str
) -> None:
    with (
        mock.patch(
            "app.main.valid_google_url", return_value=valid_google_url
        ),
        mock.patch(
            "app.main.has_internet_connection",
            return_value=has_internet_connection,
        ),
    ):
        assert can_access_google_page("www.google.com") == result
