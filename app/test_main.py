import pytest

from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,has_connection,expected",
    [
        pytest.param(
            True, True, "Accessible", id="valid url and has connection"
        ),
        pytest.param(
            True, False, "Not accessible", id="valid url and no connection"
        ),
        pytest.param(
            False, True, "Not accessible", id="invalid url and has connection"
        ),
        pytest.param(
            False, False, "Not accessible", id="invalid url and no connection"
        ),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_has_connection: mock.Mock,
        mocked_valid_url: mock.Mock,
        valid_url: bool,
        has_connection: bool,
        expected: str
) -> None:
    mocked_valid_url.return_value = valid_url
    mocked_has_connection.return_value = has_connection
    assert can_access_google_page("") == expected
