from app import main

def test_can_access_google_page(monkeypatch):
    def mock_valid_google_url(url):
        return True
    
    def mock_has_internet_connection():
        return True

    monkeypatch.setattr(main, 'valid_google_url', mock_valid_google_url)
    monkeypatch.setattr(main, 'has_internet_connection', mock_has_internet_connection)

    assert main.can_access_google_page("http://www.google.com") == "Accessible"
