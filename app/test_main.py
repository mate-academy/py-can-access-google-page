import pytest
from typing import Callable

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,connection, result",
    [
        pytest.param(True, True, "Accessible",
                     id="True url, True connection"),
        pytest.param(False, False, "Not accessible",
                     id="False url, False connection"),
        pytest.param(True, False, "Not accessible",
                     id="True url, False connection"),
        pytest.param(False, True, "Not accessible",
                     id="False url, True connection")

    ]
)
def test_access(monkeypatch: Callable,
                url: bool,
                connection: bool,
                result: str) -> None:
    monkeypatch.setattr("app.main.valid_google_url",
                        lambda *args: url)
    monkeypatch.setattr("app.main.has_internet_connection",
                        lambda *args: connection)
    assert can_access_google_page("x") == result, "unexpected result"
