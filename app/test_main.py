import pytest
from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_has_internet_connection, mocked_valid_google_url):
    test_cases = [
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible"),
        (True, False, "Not accessible")
    ]

    for has_internet, is_valid_url, expected_result in test_cases:
        mocked_has_internet_connection.return_value = has_internet
        mocked_valid_google_url.return_value = is_valid_url

        result = can_access_google_page("https://google.com")

        assert result == expected_result, (
            f"Failed for has_internet={has_internet} and is_valid_url={is_valid_url}"
        )


if __name__ == "__main__":
    pytest.main()
