from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection,url,expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        connection: bool,
        url: bool,
        expected_result: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as
        mocked_valid_google_url
    ):
        with (
            mock.patch("app.main.has_internet_connection") as
            mocked_has_internet_connection
        ):
            mocked_valid_google_url.return_value = url
            mocked_has_internet_connection.return_value = connection
            assert can_access_google_page(
                "https://www.google.com/"
            ) == expected_result
