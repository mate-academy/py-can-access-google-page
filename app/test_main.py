import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet, valid_url, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(internet: bool, valid_url: bool,
                                expected_result: str) -> None:
    path_internet = "app.main.has_internet_connection"
    path_url = "app.main.valid_google_url"

    with patch(path_internet, return_value=internet) as _, \
         patch(path_url, return_value=valid_url) as _:
        result = can_access_google_page("http://www.google.com")
        assert result == expected_result
