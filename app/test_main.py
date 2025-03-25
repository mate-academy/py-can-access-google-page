import pytest
import app.main


@pytest.mark.parametrize(
    "url, valid_google_url, has_internet_connection, output",
    [
        ("https://www.google.com/", True, True, "Accessible"),
        ("https://www.google.com/", False, True, "Not accessible"),
        ("https://www.google.com/", False, False, "Not accessible"),
        ("https://www.google.com/", True, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        monkeypatch: pytest.MonkeyPatch,
        url: str,
        valid_google_url: bool,
        has_internet_connection: bool,
        output: str
) -> None:
    def valid_url(url: str) -> bool:
        return valid_google_url

    def internet_connection() -> bool:
        return has_internet_connection
    monkeypatch.setattr(
        app.main,
        "valid_google_url",
        valid_url
    )
    monkeypatch.setattr(
        app.main,
        "has_internet_connection",
        internet_connection
    )
    assert (
        app.main.can_access_google_page(url) == output
    ), f"function should return {output} if url is {url}"
