import pytest
from typing import Any
from app import main
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_response, connection, expected",
    [
        pytest.param(
            True,
            False,
            "Not accessible",
            id="No access without connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="No access without url_response"
        ),
        pytest.param(
            True,
            True,
            "Accessible",
            id="Access is possible"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="No access without connection and url_response"
        ),
    ]
)
def test_can_access_google_page(monkeypatch: Any,
                                url_response: bool,
                                connection: bool,
                                expected: str) -> None:
    def mock_url_response(url: str) -> bool:
        return url_response

    def mock_connection() -> bool:
        return connection

    monkeypatch.setattr(main, "valid_google_url", mock_url_response)
    monkeypatch.setattr(main, "has_internet_connection", mock_connection)
    assert can_access_google_page("https://www.google.com/") == expected
