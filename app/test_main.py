import pytest
from typing import Callable
import app.main as main_module


@pytest.mark.parametrize(
    "url, expected_result, mock_valid_url, mock_internet_connection", [
        pytest.param(
            "https://google.com",
            "Accessible",
            lambda url: True,
            lambda: True,
            id="You have access to google.com."
        ),
        pytest.param(
            "https://google.com",
            "Not accessible",
            lambda url: True,
            lambda: False,
            id="You don't have internet connection."
        ),
        pytest.param(
            "https://wrong_url.com",
            "Not accessible",
            lambda url: False,
            lambda: True,
            id="Your URL is wrong."
        )
    ]
)
def test_can_access_google_page(
        monkeypatch: pytest.MonkeyPatch,
        url: str,
        expected_result: str,
        mock_valid_url: Callable,
        mock_internet_connection: Callable
) -> None:
    monkeypatch.setattr(
        main_module,
        "has_internet_connection",
        mock_internet_connection
    )
    monkeypatch.setattr(
        main_module,
        "valid_google_url",
        mock_valid_url
    )
    assert main_module.can_access_google_page(url) == expected_result
