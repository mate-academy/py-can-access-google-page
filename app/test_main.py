import pytest
from app.main import can_access_google_page
from unittest import mock


@pytest.mark.parametrize(
    "url, validator, check_connection, expected",
    [
        pytest.param(
            "https://docs.python.org/3/library/unittest.mock.html",
            True,
            True,
            "Accessible",
            id="Should return 'Access'"
        ),
        pytest.param(
            "https://docs.python.org/3/library/unittest.mock.html",
            True,
            False,
            "Not accessible",
            id="Should return 'Not Access' because no connection"
        ),
        pytest.param(
            "test",
            False,
            True,
            "Not accessible",
            id="Should return 'Not Access' because not valid url"
        ),
        pytest.param(
            "test1",
            False,
            False,
            "Not accessible",
            id="Should return 'Not Access' because no connection and url"
        )
    ]
)
def test_can_access_google_page(
        url: str,
        validator: bool,
        check_connection: bool,
        expected: str
) -> None:
    with (
        mock.patch(
            "app.main.valid_google_url",
            return_value=validator
        ),
        mock.patch(
            "app.main.has_internet_connection",
            return_value=check_connection
        )
    ):
        assert can_access_google_page(url) == expected
