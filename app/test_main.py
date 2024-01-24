import pytest
from typing import Callable
from unittest import mock


from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection_exist, url_valid, url_str, expected_result",
    [
        pytest.param(
            True, True, "https://test.com/", "Accessible",
            id="Should return Accessible \
                when connection exists and url is valid"
        ),
        pytest.param(
            False, True, "https://test.com/", "Not accessible",
            id="Should return Not accessible \
                when connection doesn't exist and url is valid"
        ),
        pytest.param(
            True, False, "https://test.com/", "Not accessible",
            id="Should return Not accessible \
                when connection exists and url is not valid"
        ),
        pytest.param(
            False, False, "https://test.com/", "Not accessible",
            id="Should return Not accessible \
                when connection doesn't exist and url is not valid"
        )
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_access_google_page(
    mocked_connection: Callable,
    mocked_url: Callable,
    connection_exist: bool,
    url_valid: bool,
    url_str: str,
    expected_result: str
) -> None:
    mocked_connection.return_value = connection_exist
    mocked_url.return_value = url_valid
    assert can_access_google_page(url_str) == expected_result
