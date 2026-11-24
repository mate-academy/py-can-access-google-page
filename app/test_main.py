import pytest

import app.main

from unittest.mock import patch


@pytest.mark.parametrize(
    "is_valid_url, is_internet, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")]
)
def test_can_access_google_page(is_valid_url: bool,
                                is_internet: bool,
                                expected: str) -> None:
    with patch("app.main.valid_google_url") as mocked_function:
        mocked_function.return_value = is_valid_url

        with patch("app.main.has_internet_connection"
                   )as another_mocked_function:
            another_mocked_function.return_value = is_internet
            assert app.main.can_access_google_page("https://www.google.com"
                                                   ) == expected
