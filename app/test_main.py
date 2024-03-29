import pytest
from _pytest.monkeypatch import MonkeyPatch
from app.main import can_access_google_page


@pytest.fixture
def url() -> str:
    return ("https://www.google.com/webhp?hl=en&sa="
            "X&ved=0ahUKEwjlr5aw25eFAxVFFBAIHbjlAdEQPAgJ")


@pytest.fixture
def mock_internet_connection_true(monkeypatch: MonkeyPatch) -> None:
    def mock_internet_connection() -> None:
        return True
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_internet_connection
    )


@pytest.fixture
def mock_internet_connection_false(monkeypatch: MonkeyPatch) -> None:
    def mock_internet_connection() -> None:
        return False
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_internet_connection
    )


@pytest.fixture
def mock_valid_google_url_true(monkeypatch: MonkeyPatch, url: str) -> None:
    def mock_valid_google_url(url: str) -> None:
        return True
    monkeypatch.setattr("app.main.valid_google_url", mock_valid_google_url)


@pytest.fixture
def mock_valid_google_url_false(monkeypatch: MonkeyPatch, url: str) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return False
    monkeypatch.setattr("app.main.valid_google_url", mock_valid_google_url)


def test_cannot_access_google_page_if_only_connection(
    url: str,
    mock_internet_connection_true: bool,
    mock_valid_google_url_false: bool
) -> None:
    assert can_access_google_page(url) == "Not accessible"


def test_cannot_access_google_page_if_only_valid_url(
    url: str,
    mock_internet_connection_false: bool,
    mock_valid_google_url_true: bool
) -> None:
    assert can_access_google_page(url) == "Not accessible"


def test_cannot_access_google_page_if_no_connection_and_valid_url(
    url: str,
    mock_internet_connection_false: bool,
    mock_valid_google_url_false: bool
) -> None:
    assert can_access_google_page(url) == "Not accessible"


def test_can_access_google_page_when_connection_and_valid_url(
    url: str,
    mock_internet_connection_true: bool,
    mock_valid_google_url_true: bool
) -> None:
    assert can_access_google_page(url) == "Accessible"
