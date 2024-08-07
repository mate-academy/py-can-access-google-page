from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet,valid_url,can_access",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible")
    ],
    ids=[
        "if has internet and valid url -> can access",
        "if doesn't have internet and not valid url -> can't access",
        "if has internet and not valid url -> can't access",
        "if doesn't have internet and valid url -> can't access",
    ]
)
def test_can_access_google_page(
        has_internet: bool,
        valid_url: bool,
        can_access: str
) -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mock_has_internet,
        mock.patch("app.main.valid_google_url")as mock_valid_url
    ):
        mock_has_internet.return_value = has_internet
        mock_valid_url.return_value = valid_url
        assert can_access_google_page("some_url") == can_access
