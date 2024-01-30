import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "google_url, internet_connection, test_result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible")
    ],
    ids=[
        "Should be Accessible when url is valid and connection is present",
        "Should not be Accessible when no valid url and no connection",
        "Should not be Accessible when url isn't valid",
        "Should not be Accessible when there is no Internet connection"
    ]
)
def test_can_access_google_page(
        google_url: str,
        internet_connection: str,
        test_result: str
) -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_url_check,
          mock.patch("app.main.has_internet_connection") as mocked_internet_check):
        mocked_url_check.return_value = google_url
        mocked_internet_check.return_value = internet_connection
        assert can_access_google_page("https://www.google.com") == test_result
