import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,connection,status",
    [
        pytest.param(
            True, True, "Accessible",
            id="Has internet connection and "
               "valid google url"
        ), pytest.param(
            False, True, "Not accessible",
            id="Valid google url but without "
               "internet connection"
        ), pytest.param(
            False, False, "Not accessible",
            id="Without internet connection and "
               "invalid google url"
        ), pytest.param(
            True, False, "Not accessible",
            id="Has internet connectionValid but "
               "invalid google url"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_page(
        mock_valid_google_url: mock.Mock,
        mock_has_internet_connection: mock.Mock,
        valid_url: bool,
        connection: bool,
        status: str
) -> None:

    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = connection

    assert can_access_google_page("https://www.google.com/") == status
