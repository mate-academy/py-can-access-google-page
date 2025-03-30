import pytest

from app.main import can_access_google_page

from unittest import mock


@pytest.mark.parametrize(
    "has_internet_connection,valid_url,expected_value",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
        has_internet_connection: bool,
        valid_url: bool,
        expected_value: str
) -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mocked_has_internet,
        mock.patch("app.main.valid_google_url") as mocked_valid_url
    ):
        mocked_valid_url.return_value = valid_url
        mocked_has_internet.return_value = has_internet_connection

        assert can_access_google_page("url") == expected_value
