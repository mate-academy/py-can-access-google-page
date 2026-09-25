from unittest.mock import patch

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    ("valid_url", "has_internet", "expected_result"),
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    valid_url: bool, has_internet: bool, expected_result: str
) -> None:
    with patch("app.main.valid_google_url", return_value=valid_url), patch(
        "app.main.has_internet_connection", return_value=has_internet
    ):
        result = can_access_google_page("https://www.google.com")

    assert result == expected_result
