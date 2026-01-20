from app.main import can_access_google_page
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "valid_url,internet_connection,expected_result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="test should return Accessible"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="test should return Not accessible"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="test should return Not accessible"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="test should return Not accessible"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: mock.Mock
        , mock_valid_google_url: mock.Mock,
        valid_url: bool,
        internet_connection: bool,
        expected_result: str) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = internet_connection
    assert (can_access_google_page("https://www.google.com/")
            == expected_result)
