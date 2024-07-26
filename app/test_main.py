from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_validator, internet_connection, access_confirmation",
    [
        pytest.param(
            True, False, "Not accessible",
            id="test when connection is invalid"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="test when url is invalid"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="test when connection and url are invalid"
        ),
        pytest.param(
            True, True, "Accessible",
            id="test when connection and url are valid"
        )
    ]

)
def test_can_access_google_page(
    url_validator: bool,
    internet_connection: bool,
    access_confirmation: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mocked_url_validator,
        mock.patch(
            "app.main.has_internet_connection"
        ) as mocked_internet_connection
    ):
        mocked_url_validator.return_value = url_validator
        mocked_internet_connection.return_value = internet_connection

        assert can_access_google_page("") == access_confirmation
