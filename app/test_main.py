import pytest
from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "valid_url, internet_connection, access",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="url valid and there is connection"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="url valid, but there is no connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="url isn't valid, but this is connection"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="url isn't valid and there is no connection"
        )
    ],
)
def test_can_access_google_page(
        mock_valid_url: mock.Mock,
        mock_internet_connection: mock.Mock,
        valid_url: bool,
        internet_connection: bool,
        access: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_internet_connection.return_value = internet_connection
    assert can_access_google_page("https://www.google.com/") == access
