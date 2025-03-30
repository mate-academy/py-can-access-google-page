from unittest import mock
from pytest import mark

from app.main import can_access_google_page


@mark.parametrize(
    "internet_connection_status, google_url_status, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mocked_url: mock.Mock,
    mocked_connection: mock.Mock,
    internet_connection_status: bool,
    google_url_status: bool,
    expected_result: str
) -> None:
    mocked_url.return_value = google_url_status
    mocked_connection.return_value = internet_connection_status

    assert (
        can_access_google_page("https://www.google.ua") == expected_result
    )
