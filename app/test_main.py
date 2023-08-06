import pytest
from _pytest.monkeypatch import MonkeyPatch
from app import main


@pytest.mark.parametrize("url, expected_result", [
    ("https://www.google.com", "Accessible"),
    ("https://www.this-url-does-not-exist.com", "Not accessible"),
    ("https://www.google.com/nonexistentpage", "Not accessible")
])
def test_can_access_google_page(
        url: str,
        expected_result: str,
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "has_internet_connection",
                        lambda: False if "nonexistentpage" in url else True)

    monkeypatch.setattr(main, "valid_google_url",
                        lambda u: True if "google" in u else False)

    assert main.can_access_google_page(url) == expected_result
