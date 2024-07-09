import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_internet, result",
    [
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (True, True, "Accessible")
    ]
)
def test_can_access_google_page(
        valid_url: bool,
        has_internet: bool,
        result: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mock_google_url,
        mock.patch("app.main.has_internet_connection") as mock_has_internet
    ):
        mock_google_url.return_value = valid_url
        mock_has_internet.return_value = has_internet
        assert can_access_google_page("google.com") == result
