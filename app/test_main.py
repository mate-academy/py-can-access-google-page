from unittest.mock import MagicMock

import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url_result,internet_connection_result,expected",
    [
        pytest.param(True, True, "Accessible",
                     id="should return accessible when "
                        "valid url and internet connection are both true"),
        pytest.param(False, True, "Not accessible",
                     id="should return not accessible "
                        "when valid url is false"),
        pytest.param(True, False, "Not accessible",
                     id="should return not accessible "
                        "when internet connection is false")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_valid_url: MagicMock,
        mocked_internet_connection: MagicMock,
        valid_url_result: bool,
        internet_connection_result: bool,
        expected: str
) -> None:
    mocked_valid_url.return_value = valid_url_result
    mocked_internet_connection.return_value = internet_connection_result

    assert can_access_google_page("url") == expected
