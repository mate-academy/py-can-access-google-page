import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_connection, is_valid, expected_access",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Accessible when all right with url and connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Not accessible when url not valid"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Not accessible when no connection"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="Not accessible when all bed with url and connection"
        )
    ]
)
def test_can_access_google_page(
        monkeypatch: pytest.MonkeyPatch,
        has_connection: bool,
        is_valid: bool,
        expected_access: str
) -> None:

    def mock_connection() -> bool:
        return has_connection

    def mock_url(url: str) -> bool:
        return is_valid

    monkeypatch.setattr("app.main.has_internet_connection", mock_connection)
    monkeypatch.setattr("app.main.valid_google_url", mock_url)
    assert can_access_google_page("www.google.com.ua") == expected_access
