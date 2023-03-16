from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,connection,expected_result",
    [
        pytest.param(False, False, "Not accessible"),
        pytest.param(False, True, "Not accessible"),
        pytest.param(True, False, "Not accessible"),
        pytest.param(True, True, "Accessible")
    ],
    ids=[
        "not accessible without connection and valid url",
        "not accessible without valid url",
        "not accessible without connection",
        "accessible with url and connection"
    ]


)
def test_(url: bool, connection: bool, expected_result: str) -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        with mock.patch("app.main.valid_google_url") as mocked_url:
            mocked_url.return_value = url
            mocked_connection.return_value = connection

            assert can_access_google_page(
                "https://www.udemy.com/"
            ) == expected_result
