import pytest
from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "initial_url, "
    "initial_flag_for_internet, "
    "initial_flag_for_url, "
    "expected_result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", False, True, "Not accessible"),
        ("https://www.google.ooo", True, False, "Not accessible"),
        ("https://www.google.ooo", False, False, "Not accessible"),
    ]
)
def test_can_access_google_page_accessible(
        mocked_has_internet_connection: mock,
        mocked_valid_google_url: mock,
        initial_url: str,
        initial_flag_for_internet: bool,
        initial_flag_for_url: bool,
        expected_result: str,
) -> None:
    mocked_has_internet_connection.return_value = initial_flag_for_internet
    mocked_valid_google_url.return_value = initial_flag_for_url
    assert can_access_google_page(initial_url) == expected_result
