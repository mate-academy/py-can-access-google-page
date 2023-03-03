from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="test should return accessible when all func true"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="test should return not accessible"
               " when internet connection false"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="test should return not accessible when valid url false"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="test should return not accessible when all func false"
        )
    ]
)
def test_should_check_function_can_access_google_page(
        valid_url: bool,
        internet_connection: bool,
        result: str
) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url,\
            mock.patch("app.main.has_internet_connection") as mocked_internet:
        mocked_url.return_value = valid_url
        mocked_internet.return_value = internet_connection
        assert can_access_google_page(
            "http://www.google.com/intl/en/privacy"
        ) == result
