import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, internet_connection, access_to_google_page",
    [
        pytest.param(
            True,
            False,
            "Not accessible",
            id="valid url, but no connection"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="not valid url and no connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="not valid url, but good connection"
        ),
        pytest.param(
            True,
            True,
            "Accessible",
            id="valid url and good connection"
        ),

    ]
)
def test_access_google_page(
        valid_google_url: bool,
        internet_connection: bool,
        access_to_google_page: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url",
                   return_value=valid_google_url),
        mock.patch("app.main.has_internet_connection",
                   return_value=internet_connection)
    ):
        assert (can_access_google_page("http://google.com")
               == access_to_google_page)
