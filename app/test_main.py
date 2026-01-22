import pytest
from typing import Any
from app import main
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_response, connection, expected_result",
    [
        pytest.param(
            True,
            False,
            "Not accessible",
            id="not accessible if not connection",
        ),
        pytest.param(
            False, True, "Not accessible", id="not accessible if not response"
        ),
    ],
)
def test_should_return_correct_result(
    monkeypatch: Any,
    url_response: bool,
    connection: bool,
    expected_result: str,
) -> None:
    def mock_response(url: str) -> bool:
        return url_response

    def mock_connection() -> bool:
        return connection

    monkeypatch.setattr(main, "valid_google_url", mock_response)

    monkeypatch.setattr(main, "has_internet_connection", mock_connection)

    assert can_access_google_page("https://www.google.com/") == expected_result
