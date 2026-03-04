from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    ("url_valid", "internet_available", "expected"),
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "accessible_when_url_valid_and_internet_available",
        "not_accessible_when_url_valid_but_no_internet",
        (
            "not_accessible_when_url_invalid_"
            "even_if_internet_available"
        ),
        "not_accessible_when_url_invalid_and_no_internet",
    ],
)
def test_can_access_google_page(
    url_valid: bool,
    internet_available: bool,
    expected: str,
) -> None:
    with mock.patch(
        "app.main.valid_google_url"
    ) as mock_valid, mock.patch(
        "app.main.has_internet_connection"
    ) as mock_internet_connection:

        mock_valid.return_value = url_valid
        mock_internet_connection.return_value = (
            internet_available
        )

        assert (
            can_access_google_page(
                "https://google.com"
            )
            == expected
        )
