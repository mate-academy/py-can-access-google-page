from collections.abc import Callable

import pytest


@pytest.fixture
def mock_dependencies(
        monkeypatch: pytest.MonkeyPatch) -> Callable[[bool, bool], None]:
    def _mock(url_valid: bool, has_connection: bool) -> None:
        monkeypatch.setattr(
            "app.main.valid_google_url",
            lambda url: url_valid)
        monkeypatch.setattr(
            "app.main.has_internet_connection",
            lambda: has_connection)
    return _mock


@pytest.mark.parametrize(
    "url_valid, has_connection, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    mock_dependencies: Callable[[bool, bool], None],
    url_valid: bool,
    has_connection: bool,
    expected: bool
) -> None:
    mock_dependencies(url_valid, has_connection)

    from app.main import can_access_google_page

    assert can_access_google_page("https://any-url.com") == expected
