from app.main import can_access_google_page


def test_accessible_google_page(monkeypatch):
    def mock_valid_google_url(url: str):
        return True
    def mock_has_internet_connection():
        return True

    monkeypatch.setattr("app.main.valid_google_url", mock_valid_google_url)
    monkeypatch.setattr("app.main.has_internet_connection", mock_has_internet_connection)

    assert can_access_google_page("") == "Accessible"


def test_not_valid_url(monkeypatch):
    def mock_valid_google_url(url: str):
        return False
    def mock_has_internet_connection():
        return True

    monkeypatch.setattr("app.main.valid_google_url", mock_valid_google_url)
    monkeypatch.setattr("app.main.has_internet_connection", mock_has_internet_connection)

    assert can_access_google_page("") == "Not accessible"


def test_has_not_internet_connection(monkeypatch):
    def mock_valid_google_url(url: str):
        return True
    def mock_has_internet_connection():
        return False

    monkeypatch.setattr("app.main.valid_google_url", mock_valid_google_url)
    monkeypatch.setattr("app.main.has_internet_connection", mock_has_internet_connection)

    assert can_access_google_page("") == "Not accessible"

def test_has_not_connection_and_not_valid_url(monkeypatch):
    def mock_valid_google_url(url: str):
        return False

    def mock_has_internet_connection():
        return False

    monkeypatch.setattr("app.main.valid_google_url", mock_valid_google_url)
    monkeypatch.setattr("app.main.has_internet_connection", mock_has_internet_connection)

    assert can_access_google_page("") == "Not accessible"
