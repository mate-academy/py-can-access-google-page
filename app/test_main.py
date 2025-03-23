import pytest
from collections.abc import Callable
from pytest import MonkeyPatch

from app.main import can_access_google_page


@pytest.fixture
def mock_dependencies(
    monkeypatch: MonkeyPatch,
) -> Callable[[bool, bool], None]:
    def apply_mocks(
        internet_connection: bool,
        valid_url: bool,
    ) -> None:
        def mock_has_internet_connection() -> bool:
            return internet_connection

        def mock_valid_google_url(url: str) -> bool:
            return valid_url

        monkeypatch.setattr(
            "app.main.has_internet_connection",
            mock_has_internet_connection,
        )
        monkeypatch.setattr(
            "app.main.valid_google_url",
            mock_valid_google_url,
        )

    return apply_mocks


@pytest.mark.parametrize(
    ("internet_connection", "valid_url", "expected_result"),
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    mock_dependencies: Callable[[bool, bool], None],
    internet_connection: bool,
    valid_url: bool,
    expected_result: str,
) -> None:
    mock_dependencies(internet_connection, valid_url)

    result = can_access_google_page("https://www.google.com")

    assert result == expected_result
