from unittest import mock

import pytest

from app.main import can_access_google_page


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
        valid_url: bool,
        has_connection: bool,
        access: str
) -> None:

    with mock.patch("app.main.has_internet_connection") as mock_has_internet:
        mock_has_internet.return_value = has_connection
        with mock.patch("app.main.valid_google_url") as mock_valid_google_url:
            mock_valid_google_url.return_value = valid_url
            assert can_access_google_page("") == access
