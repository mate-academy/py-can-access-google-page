import pytest
from app.main import can_access_google_page
from unittest import mock

@pytest.mark.parametrize(
    "valid_url,has_connection,expected",
    [
        pytest.param(True, True, "Accessible",
                     id="valid url and has connection"),
        pytest.param(True, False, "Not accessible",
                     id="valid url and no connection"),
        pytest.param(False, True, "Not accessible",
                     id="invalid url and has connection"),
        pytest.param(False, False, "Not accessible",
                     id="invalid url and no connection"),
    ]
)
def test_can_access_google_page(
        valid_url: bool,
        has_connection: bool,
        expected: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mocked_valid_url,
        mock.patch("app.main.has_internet_connection") as mocked_has_connection
    ):
        mocked_valid_url.return_value = valid_url
        mocked_has_connection.return_value = has_connection
        assert can_access_google_page("") == expected
