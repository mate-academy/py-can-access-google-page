import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "current_time,current_url,exception_message",
    [
        (
            True,
            True,
            "Accessible"
        ),
        (
            False,
            True,
            "Not accessible"
        ),
        (
            True,
            False,
            "Not accessible"
        ),
        (
            False,
            False,
            "Not accessible"
        )
    ]
)
def test_can_access_to_page(
        current_time: bool,
        current_url: bool,
        exception_message: str
) -> None:
    with mock.patch("app.main.valid_google_url") as mock_url:
        with mock.patch("app.main.has_internet_connection") as mock_connection:
            mock_url.return_value = current_url
            mock_connection.return_value = current_time
            assert can_access_google_page("google.com") == exception_message
