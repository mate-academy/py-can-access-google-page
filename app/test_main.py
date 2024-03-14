from app.main import can_access_google_page
from unittest import mock
import pytest
import datetime
import requests


@pytest.mark.parametrize(
    "valid_google_url_value, has_internet_connection_value, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        valid_google_url_value: bool,
        has_internet_connection_value: bool,
        expected_result: str
) -> None:
    with mock.patch(
            "app.main.valid_google_url",
            return_value=valid_google_url_value
    ), mock.patch(
        "app.main.has_internet_connection",
        return_value=has_internet_connection_value
    ):
        assert can_access_google_page(
            "https://www.google.com"
        ) == expected_result


def test_real_can_access_google_page() -> None:
    if (requests.get("https://www.google.com").status_code == 200
            and datetime.datetime.now().hour in range(6, 23)):
        assert can_access_google_page(
            "https://www.google.com"
        ) == "Accessible"
    else:
        assert can_access_google_page(
            "https://www.google.com"
        ) == "Not accessible"
