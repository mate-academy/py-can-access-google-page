import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_validation, internet_connection, access",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "True True must give Access",
        "True False must give Not Access",
        "False True must give Not Access",
        "False False must give Not Access"
    ]

)
def test_can_access_google_page(
        url_validation: bool,
        internet_connection: bool,
        access: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url",
                   return_value=url_validation),
        mock.patch("app.main.has_internet_connection",
                   return_value=internet_connection)
    ):
        assert can_access_google_page("test") == access
