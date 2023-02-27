from unittest import mock

import pytest

from .main import can_access_google_page


@pytest.mark.parametrize(
    "status,internet_connection,ability_to_access",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_internet: mock,
        mocked_google_url: mock,
        status: bool,
        internet_connection: bool,
        ability_to_access: str
) -> None:
    url = "google.com"
    mocked_google_url.return_value = status
    mocked_internet.return_value = internet_connection

    assert can_access_google_page(url) == ability_to_access
