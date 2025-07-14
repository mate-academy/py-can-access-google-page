import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection, valid_url, url, expected", [
        (
            True,
            True,
            "https://en.wikipedia.org/wiki/Hello_Kitty",
            "Accessible"
        ),
        (
            True,
            False,
            "https://en.wikipedia.org/?title=Kuromi&redirect=no",
            "Not accessible"
        ),
        (
            False,
            True,
            "https://en.wikipedia.org/wiki/Mortal_Kombat",
            "Not accessible"
        ),
        (
            False,
            False,
            "https://en.wikipedia.org/wiki/Pusheen",
            "Not accessible"
        )
    ]
)
def test_can_access_google_page(
        connection: bool,
        valid_url: bool,
        url: str,
        expected: str
) -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_url,
          mock.patch("app.main.has_internet_connection") as mocked_time):
        mocked_time.return_value = connection
        mocked_url.return_value = valid_url
        assert (
            can_access_google_page(url) == expected
        )
