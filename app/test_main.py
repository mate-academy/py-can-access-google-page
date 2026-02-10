from app.main import can_access_google_page


def test_valid_url_and_connection_exists() -> None:
    assert can_access_google_page("https://google.com") == "Accessible"
    assert can_access_google_page("https://not-exist.com") == "Not accessible"
