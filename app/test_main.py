from app.main import can_access_google_page


def test_can_acces_google_page_for_acessible() -> None:
    url = "https://example.com"
    assert can_access_google_page(url) == "Accessible"


def test_can_acces_google_page_for_not_acessible() -> None:
    url = "https://example.com/nonexistentpage"
    assert can_access_google_page(url) == "Not accessible"
