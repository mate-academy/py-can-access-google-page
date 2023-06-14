from unittest import mock
from typing import Callable


from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mocked_valid: Callable,
    mocked_connection: Callable
) -> None:
    mocked_connection.return_value = True
    mocked_valid.return_value = True
    assert (
        can_access_google_page("https://www.youtube.com/") == "Accessible"
    )

    mocked_connection.return_value = False
    mocked_valid.return_value = True
    assert (
        can_access_google_page("https://www.youtube.com/") == "Not accessible"
    )

    mocked_connection.return_value = True
    mocked_valid.return_value = False
    assert (
        can_access_google_page("https:/ww.you1t1u1be.com/") == "Not accessible"
    )
