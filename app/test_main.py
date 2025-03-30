import pytest
import app.main as main
from typing import Callable


@pytest.mark.parametrize(
    "url, expected, mock_valid, mock_internet",
    [
        pytest.param(
            "https://google.com",
            "Not accessible",
            lambda url: True,
            lambda: False,
            id="No Internet",
        ),
        pytest.param(
            "",
            "Not accessible",
            lambda url: False,
            lambda: True,
            id="Invalid URL",
        ),
        pytest.param(
            "https://google.com",
            "Accessible",
            lambda url: True,
            lambda: True,
            id="Access Google",
        ),
        pytest.param(
            "https://www.google.com",
            "Accessible",
            lambda url: True,
            lambda: True,
            id="Access www.google",
        ),
    ],
)
def test_can_access_google_page(
    monkeypatch: pytest.MonkeyPatch,
    url: str,
    expected: str,
    mock_valid: Callable[[str], bool],
    mock_internet: Callable[[], bool],
) -> None:
    monkeypatch.setattr(main, "has_internet_connection", mock_internet)
    monkeypatch.setattr(main, "valid_google_url", mock_valid)

    assert main.can_access_google_page(url) == expected
