import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection, url_valid, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        connection: bool,
        url_valid: bool,
        expected_result: str
) -> None:
    with (patch("app.main.has_internet_connection", return_value=connection)):
        with patch("app.main.valid_google_url", return_value=url_valid):
            assert can_access_google_page(
                "https://mate.academy"
            ) == expected_result
