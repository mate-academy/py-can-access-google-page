from typing import Any
from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_combined_conditions(
        mocked_valid_google_url: Any,
        mocked_has_internet_connection: Any
) -> None:
    # Define test cases with combinations
    test_cases = [
        (False, False, False),
        (False, True, False),
        (True, True, True),
        (True, False, False)
    ]

    for has_internet, is_valid_url, expected_result in test_cases:
        mocked_has_internet_connection.return_value = has_internet
        mocked_valid_google_url.return_value = is_valid_url

        result = can_access_google_page("https://google.com")

        assert result == expected_result, (
            f"Failed for has_internet={has_internet} and is_valid_url={is_valid_url}"
        )

    mocked_has_internet_connection.assert_called()
    mocked_valid_google_url.assert_called_with("https://google.com")
