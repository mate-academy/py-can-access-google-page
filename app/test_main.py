import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_validation, connection_validation, result",
    [
        pytest.param(True, True, "Accessible",
                     id="Test if all correct value"),
        pytest.param(True, False, "Not accessible",
                     id="Test if correct url"),
        pytest.param(False, True, "Not accessible",
                     id="Test if correct time"),
        pytest.param(False, False, "Not accessible",
                     id="Test if not correct url and time"),
    ]
)
def test_can_access_google_page(
        url_validation: bool,
        connection_validation: bool,
        result: str
) -> None:
    with (mock.patch("app.main.valid_google_url") as valid_google_url,
          mock.patch(
              "app.main.has_internet_connection") as has_internet_connection):
        has_internet_connection.return_value = connection_validation
        valid_google_url.return_value = url_validation
        assert can_access_google_page("https://google.com/") == result
