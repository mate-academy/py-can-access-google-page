import pytest
from unittest.mock import patch

from .main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection_result,valid_url_result,result",
    [
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible"),
    ]
)
def test_if_can_access_google_page_return_correct_str(
        has_internet_connection_result,
        valid_url_result,
        result) -> None:
    with patch("app.main.has_internet_connection",
               return_value=has_internet_connection_result), \
        patch("app.main.valid_google_url",
              return_value=valid_url_result):
        assert can_access_google_page("url.example") == result
