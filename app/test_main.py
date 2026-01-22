import pytest

from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, is_exist_connection, result, test_id",
    [
        (True,
         True,
         "Accessible",
         "'Accessible' when url is valid and connection exist"),
        (False,
         True,
         "Not accessible",
         "'Not accessible' when url isn't valid and connection exist"),
        (True,
         False,
         "Not accessible",
         "'Not accessible' when url is valid and connection doesn't exist"),
        (False,
         False,
         "Not accessible",
         "'Not accessible' when url isn't valid and connection doesn't exist"),
    ]
)
def test_can_access_google_page(
        is_valid_url: bool,
        is_exist_connection: bool,
        result: str,
        test_id: str
) -> None:
    with (
        patch("app.main.valid_google_url") as mock_google_url,
        patch("app.main.has_internet_connection") as mock_internet_connection
    ):
        mock_google_url.return_value = is_valid_url
        mock_internet_connection.return_value = is_exist_connection
        assert can_access_google_page(
            "https://www.google.com."
        ) == result, test_id
