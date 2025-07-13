from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, is_valid, has_connection, expected",
    [
        pytest.param(
            "https://www.youtube.com",
            True,
            True,
            "Accessible",
            id="test when url is valid and have internet connection"
        ),
        pytest.param(
            "https:/w.youube.com",
            False,
            True,
            "Not accessible",
            id="test when url is not valid"
        ),
        pytest.param(
            "https://www.youtube.com",
            True,
            False,
            "Not accessible",
            id="test when no internet connection"
        ),
        pytest.param(
            "htps://youtube.net",
            False,
            False,
            "Not accessible",
            id="test when no internet connection and url is not valid"
        )
    ]

)
def test_can_access_google_page(
        url: str,
        is_valid: bool,
        has_connection: bool,
        expected: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mocked_url,
        mock.patch("app.main.has_internet_connection") as mocked_connection
    ):
        mocked_url.return_value = is_valid
        mocked_connection.return_value = has_connection

        assert can_access_google_page(url) == expected
