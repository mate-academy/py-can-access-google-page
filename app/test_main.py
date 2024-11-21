from unittest import mock

import pytest

from app.main import can_access_google_page

from typing import Callable


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "valid_google_url, internet_connection, expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="should return `Accessible` if all `True`"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="should return `Not accessible` if all `False`"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="should return `Not accessible` if valid_google_url is `False`"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id=("should return `Not accessible` if "
                "internet_connection is `False`")
        ),
    ]
)
def test_can_access_google_page(
        mock_valid_google_url: Callable,
        mock_has_internet_connection: Callable,
        valid_google_url: bool,
        internet_connection: bool,
        expected: str
) -> None:
    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet_connection.return_value = internet_connection

    assert can_access_google_page("https://www.google.com/") == expected
