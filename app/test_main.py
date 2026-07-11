import pytest
import app.main


from typing import Any, Callable


from app.main import can_access_google_page


def mock_true(*args, **kwargs) -> bool:
    return True


def mock_false(*args, **kwargs) -> bool:
    return False


@pytest.mark.parametrize(
    "url,internet,result",
    [
        (mock_false, mock_true, "Not accessible"),
        (mock_true, mock_false, "Not accessible"),
        (mock_true, mock_true, "Accessible")
    ]
)
def test_returns_accessible_if_url_valid_and_has_internet(
    monkeypatch: Any,
    url: Callable,
    internet: Callable,
    result: str
) -> None:
    monkeypatch.setattr(app.main, "valid_google_url", url)
    monkeypatch.setattr(app.main, "has_internet_connection", internet)

    assert can_access_google_page("https://google.com") == result
