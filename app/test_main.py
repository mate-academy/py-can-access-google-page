import pytest
from typing import Callable
from app.main import can_access_google_page
import app.main as main


@pytest.mark.parametrize(
    "mock_connected,mock_valid,expected_result",
    [
        pytest.param(
            lambda: True,
            lambda *args, **kwargs: True,
            "Accessible",
            id="should give access due to valid url and existing connection"
        ),
        pytest.param(
            lambda: False,
            lambda *args, **kwargs: True,
            "Not accessible",
            id="should deny access when there is no internet connection"
        ),
        pytest.param(
            lambda: True,
            lambda *args, **kwargs: False,
            "Not accessible",
            id="should deny access when there is not valid link"
        ),
        pytest.param(
            lambda: True,
            lambda *args, **kwargs: False,
            "Not accessible",
            id="should deny access because there is not "
               "valid url and existing connection"
        )
    ]
)
def test_can_access_google_page(
        monkeypatch: pytest.MonkeyPatch,
        mock_valid: Callable,
        mock_connected: Callable,
        expected_result: str
) -> None:
    monkeypatch.setattr(main, "has_internet_connection", mock_connected)
    monkeypatch.setattr(main, "valid_google_url", mock_valid)
    assert can_access_google_page("https://www.google.com") == expected_result
