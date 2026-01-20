from unittest import mock

import pytest

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "valid_url,"
    "has_connection,"
    "access", [
        pytest.param(
            True, True,
            "Accessible",
            id="Test 'Accessible' if url: 'True', connection: 'True'"
        ),
        pytest.param(
            False, False,
            "Not accessible",
            id="Test 'Not accessible' if url: 'False', connection: 'False'"
        ),
        pytest.param(
            True, False,
            "Not accessible",
            id="Test 'Not accessible' if url: 'True', connection: 'False'"
        ),
        pytest.param(
            False, True,
            "Not accessible",
            id="Test 'Not accessible' if url: 'False', connection: 'True'"

        )
    ]
)
def test_access_google_page(
        mock_valid_url: mock.Mock,
        mock_connection: mock.Mock,
        valid_url: bool,
        has_connection: bool,
        access: str
) -> None:

    mock_valid_url.return_value = valid_url
    mock_connection.return_value = has_connection

    assert can_access_google_page("") == access
