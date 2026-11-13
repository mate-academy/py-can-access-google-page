from unittest.mock import patch

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
    valid_url: bool,
    internet: bool,
    expected: str
) -> None:
    with (
        patch(
            "app.main.valid_google_url",
            return_value=valid_url
        ) as mock_url,
        patch(
            "app.main.has_internet_connection",
            return_value=internet
        ) as mock_internet
    ):
        result = can_access_google_page(
            "https://www.google.com"
        )

        assert result == expected
        mock_internet.assert_called_once_with()

        if internet:
            mock_url.assert_called_once_with(
                "https://www.google.com"
            )
        else:
            mock_url.assert_not_called()
