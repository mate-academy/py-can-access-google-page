import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Valid URL with Internet Connection"
        ),

        pytest.param(
            False,
            False,
            "Not accessible",
            id="Invalid url and invalid Internet Connection"
        ),

        pytest.param(
            False,
            True,
            "Not accessible",
            id="Invalid url and  valid Internet Connection"
        ),

        pytest.param(
            True,
            False,
            "Not accessible",
            id="Valid url and invalid Internet Connection"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock,
        valid_google_url: str,
        has_internet_connection: bool,
        expected: str
) -> None:

    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet_connection.return_value = has_internet_connection
    assert can_access_google_page("https://google.com/") == expected
