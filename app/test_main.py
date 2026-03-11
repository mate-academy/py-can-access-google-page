from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,conn,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
        url: bool,
        conn: bool,
        expected: str,
) -> None:
    with (mock.patch("app.main.valid_google_url", return_value=url),
          mock.patch("app.main.has_internet_connection", return_value=conn)):
        assert can_access_google_page("") == expected
