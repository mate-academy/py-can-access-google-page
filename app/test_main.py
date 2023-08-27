import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_url_valid, is_connection, is_access",
    [
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible")
    ],
    ids=[
        "url isn't valid and there is no connection",
        "url valid, but there is no connection",
        "url isn't valid, but this is connection",
        "url valid and there is connection"
    ]
)
def test_access_to_google_page(
    is_url_valid: bool, is_connection: bool, is_access: bool
) -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_url,
          mock.patch("app.main.has_internet_connection") as mocked_connection):
        mocked_url.return_value = is_url_valid
        mocked_connection.return_value = is_connection
        assert can_access_google_page("https://www.google.com/") == is_access
