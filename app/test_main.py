import app.main
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "url_validation,connection_validation,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_valid_url_and_connection_exists(
        url_validation: bool,
        connection_validation: bool,
        result: str
) -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mocked_connection,
        mock.patch("app.main.valid_google_url") as mocked_valid_google_url
    ):
        mocked_connection.return_value = connection_validation
        mocked_valid_google_url.return_value = url_validation
        assert app.main.can_access_google_page("") == result
