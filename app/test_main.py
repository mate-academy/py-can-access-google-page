from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_connection, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "should be 'Accessible' when url is valid and has connection",
        "should be 'Not accessible' when url is NOT valid and has connection",
        "should be 'Not accessible' when url is valid and has NO connection",
        ("should be 'Not accessible' when "
         "url is NOT valid and has NO connection"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_url: mock.MagicMock,
        mock_has_connection: mock.MagicMock,
        valid_url: bool,
        has_connection: bool,
        expected_result: str

) -> None:
    mock_valid_url.return_value = valid_url
    mock_has_connection.return_value = has_connection
    assert can_access_google_page("valid_url") == expected_result
