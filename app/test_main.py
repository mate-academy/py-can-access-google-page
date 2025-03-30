import pytest
from unittest import mock
from app import main


@pytest.mark.parametrize(
    "internet_connection, is_valid_url, outcome",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        internet_connection: bool, is_valid_url: bool, outcome: str
) -> bool:
    with (
        mock.patch("app.main.has_internet_connection",
                   return_value=internet_connection),
        mock.patch("app.main.valid_google_url",
                   return_value=is_valid_url)
    ):
        result = main.can_access_google_page("https://www.google.com/")

        assert result == outcome
