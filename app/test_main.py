import pytest
from unittest import mock
from app import main


@pytest.mark.parametrize("has_internet, is_valid_url, expected_result", [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible")
])
def test_can_access_google_page(
        has_internet: bool,
        is_valid_url: bool,
        expected_result: str
) -> None:

    with mock.patch("app.main.has_internet_connection",
                    return_value=has_internet):
        with mock.patch("app.main.valid_google_url",
                        return_value=is_valid_url):
            assert main.can_access_google_page("") == expected_result
