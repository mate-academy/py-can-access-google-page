import pytest
from unittest import mock
import app.main


@pytest.mark.parametrize(
    "google_url, internet_connection, result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
    ],
    ids=[
        "correct google url, correct connection",
        "bad google url, bad connection",
        "correct google url, bad connection",
        "bad google url, correct connection",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_google_url: mock.MagicMock,
        mock_internet_connection: mock.MagicMock,
        google_url: bool,
        internet_connection: bool,
        result: str
) -> None:
    mock_google_url.return_value = google_url
    mock_internet_connection.return_value = internet_connection
    assert app.main.can_access_google_page("google.com") == result
