from unittest import mock

import pytest

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "url_status, has_connection_status, expected_message",
    [
        pytest.param(True, True, "Accessible",
                     id="Return Accessible if all is True"),

        pytest.param(True, False, "Not accessible",
                     id="Return Not accessible if all is False"),

        pytest.param(False, True, "Not accessible",
                     id="Return Not accessible if url_status is False"),

        pytest.param(False, False, "Not accessible",
                     id="Return Not accessible if "
                        "has_connection_status is False")
    ]
)
def test_can_access_google_page(
        mocked_url_validation: callable,
        mocked_connection: callable,
        url_status: bool,
        has_connection_status: bool,
        expected_message: str
) -> None:

    mocked_url_validation.return_value = url_status
    mocked_connection.return_value = has_connection_status
    assert can_access_google_page("url") == expected_message
