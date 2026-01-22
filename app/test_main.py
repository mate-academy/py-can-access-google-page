import pytest
from typing import Any
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,internet_connection,result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_should_return_if_can_access_to_page(
        monkeypatch: Any,
        valid_url: bool,
        internet_connection: bool,
        result: str,
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: valid_url)
    monkeypatch.setattr("app.main.has_internet_connection",
                        lambda: internet_connection
                        )
    assert (
        can_access_google_page("https://www.google.com") == result
    )
