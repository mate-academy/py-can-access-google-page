import app.main
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "url, connection, expected",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        monkeypatch: object,
        url: bool,
        connection: bool,
        expected: str
) -> None:
    with (mock.patch("app.main.valid_google_url",
                     return_value=url),
          mock.patch("app.main.has_internet_connection",
                     return_value=connection)):
        assert app.main.can_access_google_page(url) == expected
