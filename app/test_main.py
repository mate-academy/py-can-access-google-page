import pytest
from unittest import mock
from app import main


@pytest.mark.parametrize(
    "has_internet_connection, valid_google_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        has_internet_connection,
        valid_google_url,
        expected
):
    with mock.patch(
            "app.main.has_internet_connection",
            return_value=has_internet_connection
    ):
        with mock.patch(
                "app.main.valid_google_url",
                return_value=valid_google_url
        ):
            result = main.can_access_google_page("https://www.google.com")
    assert result == expected
