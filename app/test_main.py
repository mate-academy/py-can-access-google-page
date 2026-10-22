import pytest
from unittest import mock
from app import main


@pytest.mark.parametrize(
    "valid_url, connection, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    valid_url: bool,
    connection: bool,
    expected: str,
) -> None:
    with mock.patch(
        "app.main.valid_google_url", return_value=valid_url
    ), mock.patch("app.main.has_internet_connection", return_value=connection):
        assert (
            main.can_access_google_page("https://www.google.com") == expected
        )
