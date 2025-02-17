from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_valid_url,mock_internet_connection, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        mock_valid_url: bool,
        mock_internet_connection: bool,
        expected_result: str
) -> None:
    with mock.patch(
            "app.main.valid_google_url",
            return_value=mock_valid_url
    ), mock.patch(
            "app.main.has_internet_connection",
            return_value=mock_internet_connection
    ):
        assert can_access_google_page(
            "https://www.google.com"
        ) == expected_result
