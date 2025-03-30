import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, internet_connection, access_status", [
        pytest.param(
            False,
            False,
            "Not accessible",
            id="should return not accessible when url and time is wrong"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="should return not accessible when no internet"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="should return not accessible when wrong url"
        ),
        pytest.param(
            True,
            True,
            "Accessible",
            id="should return accessible when url and time correct"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_page(
        mock_valid_url: mock.Mock,
        mock_has_internet: mock.Mock,
        url: bool,
        internet_connection: bool,
        access_status: str
) -> None:
    mock_valid_url.return_value = url
    mock_has_internet.return_value = internet_connection

    assert can_access_google_page("https://www.google.com/") == access_status
