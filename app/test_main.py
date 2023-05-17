from unittest import mock

import pytest

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "url, connection, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Accessible if valid url and has connection",
        "Not accessible if not valid url and has connection",
        "Not accessible if valid url and has not connection",
        "Not accessible if not valid url and has not connection",
    ]
)
def test_url_and_connection(mocked_url: mock.MagicMock,
                            mocked_connection: mock.MagicMock,
                            url: bool,
                            connection: bool,
                            expected: str,
                            ) -> None:
    mocked_url.return_value = url
    mocked_connection.return_value = connection
    assert can_access_google_page(
        "https://www.google.com"
    ) == expected
