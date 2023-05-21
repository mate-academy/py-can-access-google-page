import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "page_is_valid,has_internet,result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ]
)
def test_can_access_google_page(
        page_is_valid: bool,
        has_internet: bool,
        result: str
) -> None:
    with (mock.patch("app.main.valid_google_url")
          as mocked_valid_google_url,
          mock.patch("app.main.has_internet_connection")
          as mocked_has_internet_connection):

        mocked_valid_google_url.return_value = page_is_valid
        mocked_has_internet_connection.return_value = has_internet
        assert can_access_google_page("") == result
