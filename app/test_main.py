import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_validation, time_validation, access",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        url_validation: bool,
        time_validation: bool,
        access: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url",
                   return_value=url_validation),
        mock.patch("app.main.has_internet_connection",
                   return_value=time_validation)
    ):
        assert can_access_google_page("https://www.google.com") == access
