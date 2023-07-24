from unittest import mock
import pytest

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
        "internet_connection, is_valid_url, outcome",
        [
            (True, True, "Accessible"),
            (True, False, "Not accessible"),
            (False, True, "Not accessible"),
            (False, False, "Not accessible")
        ]
)
def test_how_the_function_works(
        mocked_connection,
        mocked_valid_url,
        internet_connection: bool,
        is_valid_url: bool,
        outcome: str
    ) -> None:
    mocked_connection.return_value = internet_connection
    mocked_valid_url.return_value = is_valid_url
    assert can_access_google_page("") == outcome
