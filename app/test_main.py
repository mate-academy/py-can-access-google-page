import pytest

from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,internet_connection,return_value",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="valid url and has internet connection"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="valid url and has no internet connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="invalid url and has internet connection"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="invalid url and has no internet connection"
        ),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_invalid_url_and_has_internet_connection(
        mock_valid_url: mock,
        mock_has_connection: mock,
        valid_url: bool,
        internet_connection: bool,
        return_value: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_has_connection.return_value = internet_connection

    assert can_access_google_page("https://www.google.com/") == return_value
