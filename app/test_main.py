import pytest
from app.main import can_access_google_page


def mock_valid_google_url(url: str) -> bool:
    return url == "https://www.google.com"


def mock_has_internet_connection() -> bool:
    from datetime import datetime
    now: datetime.time = datetime.now().time()
    return (now >= datetime.strptime("06:00:00", "%H:%M:%S").time()
            and now <= datetime.strptime("22:59:59", "%H:%M:%S").time())


@pytest.mark.parametrize("url, internet_status, expected", [
    pytest.param(
        "https://www.google.com",
        True,
        "Accessible",
        id="valid_url_with_internet"
    ),
    pytest.param(
        "https://www.google.com",
        False,
        "Not accessible",
        id="valid_url_no_internet"
    ),
    pytest.param(
        "https://example.com",
        True,
        "Not accessible",
        id="invalid_url_with_internet"
    ),
    pytest.param(
        "https://example.com",
        False,
        "Not accessible",
        id="invalid_url_no_internet"
    ),
])
def test_can_access_google_page(
        monkeypatch: pytest.MonkeyPatch,
        url: str,
        internet_status: bool,
        expected: str
) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda x: mock_valid_google_url(x)
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: internet_status
    )
    assert can_access_google_page(url) == expected
