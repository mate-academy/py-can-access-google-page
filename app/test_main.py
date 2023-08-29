import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, expected_message",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="test access if valid url and has connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="test access if not valid url and has connection"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="test access if valid url and has not connection"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="test access if not valid url and has not connection"
        )
    ]
)
def test_can_access_if_has_connection_and_valid_url(
        valid_google_url: bool,
        has_internet_connection: bool,
        expected_message: str
) -> None:
    assert can_access_google_page("url") == expected_message
