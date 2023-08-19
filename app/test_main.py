import pytest
from unittest import mock


from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connected, valid_google_url, can_access",
    (
        pytest.param(True, True,
                     "Accessible",
                     id="Has connection and valid url"),
        pytest.param(False, True,
                     "Not accessible",
                     id="No connection but valid url"),
        pytest.param(True, False,
                     "Not accessible",
                     id="Has connection invalid url")
    )
)
def test_can_access_google_page(internet_connected: bool,
                                valid_google_url: bool,
                                can_access: str) -> None:
    with mock.patch("app.main.has_internet_connection") as connection:
        with mock.patch("app.main.valid_google_url") as url_validator:
            connection.return_value = internet_connected
            url_validator.return_value = valid_google_url

            assert can_access_google_page("any.com") == can_access
