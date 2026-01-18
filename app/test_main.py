import pytest

from app.main import can_access_google_page
from unittest.mock import patch


@pytest.mark.parametrize(
    "internet, valid_url, result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page_for_all_scenarios(
        internet: bool,
        valid_url: bool,
        result: str
) -> None:
    with (patch("app.main.has_internet_connection")
          as mocked_has_internet_connection,
            patch("app.main.valid_google_url") as mocked_valid_google_url):
        mocked_has_internet_connection.return_value = internet
        mocked_valid_google_url.return_value = valid_url
        assert can_access_google_page("some.address") == result
