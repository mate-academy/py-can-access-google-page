import pytest

from unittest import mock

from _pytest.monkeypatch import MonkeyPatch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url_value, connection_value, expected_value",
    [
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (True, True, "Accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page(
        mock_has_internet_connection: "MonkeyPatch",
        mock_valid_google_url: "MonkeyPatch",
        valid_url_value: bool,
        connection_value: bool,
        expected_value: str
) -> None:

    mock_has_internet_connection.return_value = connection_value
    mock_valid_google_url.return_value = valid_url_value
    url = "https://www.google.com"
    assert can_access_google_page(url) == expected_value
