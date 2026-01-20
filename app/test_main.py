from app import main


def mock_valid_google_url_true(url: str) -> bool:
    return True


def mock_valid_google_url_false(url: str) -> bool:
    return False


def mock_has_internet_connection_true() -> bool:
    return True


def mock_has_internet_connection_false() -> bool:
    return False


def test_can_access_google_page(monkeypatch):
    monkeypatch.setattr(main, 'valid_google_url', mock_valid_google_url_true)
    monkeypatch.setattr(main, 'has_internet_connection', mock_has_internet_connection_true)

    assert main.can_access_google_page("http://www.google.com") == "Accessible"


def test_cannot_access_google_page_no_connection(monkeypatch):
    monkeypatch.setattr(main, 'valid_google_url', mock_valid_google_url_true)
    monkeypatch.setattr(main, 'has_internet_connection', mock_has_internet_connection_false)

    assert main.can_access_google_page("http://www.google.com") == "Not accessible"


def test_cannot_access_google_page_invalid_url(monkeypatch):
    monkeypatch.setattr(main, 'valid_google_url', mock_valid_google_url_false)
    monkeypatch.setattr(main, 'has_internet_connection', mock_has_internet_connection_true)

    assert main.can_access_google_page("http://www.google.com") == "Not accessible"


def test_cannot_access_google_page_no_connection_no_valid_url(monkeypatch):
    monkeypatch.setattr(main, 'valid_google_url', mock_valid_google_url_false)
    monkeypatch.setattr(main, 'has_internet_connection', mock_has_internet_connection_false)

    assert main.can_access_google_page("http://www.google.com") == "Not accessible"
