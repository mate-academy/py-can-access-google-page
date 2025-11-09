import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url_return, internet_return, expected",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://google.com", True, False, "Not accessible"),
        ("https://yandex.ru", False, True, "Not accessible"),
        ("https://yandex.ru", False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    monkeypatch: pytest.MonkeyPatch,
    url: str,
    valid_url_return: bool,
    internet_return: bool,
    expected: str,
) -> None:
    monkeypatch.setattr("app.main.valid_google_url",
                        lambda _: valid_url_return)
    monkeypatch.setattr("app.main.has_internet_connection",
                        lambda: internet_return)
    result = can_access_google_page(url)
    assert result == expected
