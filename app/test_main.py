import pytest

import app.main


@pytest.mark.parametrize(
    "url,hour,result",
    [
        ("https://www.google.com", 6, "Accessible"),
        ("https://www.google.co.uk", 6, "Accessible"),
        ("https://www.google.de", 6, "Accessible"),
        ("https://www.google.me", 6, "Not accessible"),
        ("https://www.g00gle.com", 6, "Not accessible"),
        ("https://www.google.com", 24, "Not accessible"),
        ("https://www.google.com", 23, "Not accessible"),
        ("", 6, "Not accessible"),
        ("https://www.google.com", 5, "Not accessible")
    ]
)
def test_can_access_google_page(
        monkeypatch: pytest.MonkeyPatch,
        url: str,
        hour: int,
        result: str
) -> None:

    def fake_valid_google_url(url: str) -> bool:
        valid_list = [
            "https://www.google.com",
            "https://www.google.co.uk",
            "https://www.google.de"
        ]
        return url in valid_list

    monkeypatch.setattr(
        app.main,
        "valid_google_url",
        fake_valid_google_url
    )

    def fake_has_internet_connection() -> bool:
        return hour in range(6, 23)

    monkeypatch.setattr(
        app.main,
        "has_internet_connection",
        fake_has_internet_connection
    )

    assert (app.main.can_access_google_page(url) == result), \
        f"Failed: URL {url} and hour {hour} returned '{result}'"
