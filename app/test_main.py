import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "google_url_value, connection_value, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_function(
        mocked_connection: None,
        mocked_url: None,
        google_url_value: bool,
        connection_value: bool,
        result: str
) -> None:
    mocked_url.return_value = google_url_value
    mocked_connection.return_value = connection_value

    assert can_access_google_page("mate.academy") == result
