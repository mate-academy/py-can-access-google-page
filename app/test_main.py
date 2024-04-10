import pytest
from unittest.mock import MagicMock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible")
    ]
)
def test_can_access_google_page(mocker: MagicMock,
                                valid_google_url: bool,
                                has_internet_connection: bool,
                                expected_result: str) -> None:
    mocker.patch("app.main.valid_google_url",
                 return_value=valid_google_url)
    mocker.patch("app.main.has_internet_connection",
                 return_value=has_internet_connection)

    assert can_access_google_page("https://www.google.com") == expected_result
