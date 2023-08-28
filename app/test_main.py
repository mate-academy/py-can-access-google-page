import pytest

from app import main

from typing import Callable


@pytest.mark.parametrize(
    "url, mock_url, mock_internet, expected_result",
    [
        pytest.param(
            "",
            lambda: True,
            lambda: False,
            "Not accessible",
        ),
        pytest.param(
            "https://google.com",
            lambda url: True,
            lambda: True,
            "Accessible",
        ),
        pytest.param(
            "https://www.google.com",
            lambda url: True,
            lambda: True,
            "Accessible",
        ),
        pytest.param(
            "https://www.google.com",
            lambda url: False,
            lambda: True,
            "Not accessible",
        )
    ]
)
def test_can_access_google_page(
    monkeypatch: pytest.MonkeyPatch,
    url: str,
    mock_url: Callable,
    mock_internet: Callable,
    expected_result: str
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", mock_url)
    monkeypatch.setattr("app.main.has_internet_connection", mock_internet)

    assert main.can_access_google_page(url) == expected_result
