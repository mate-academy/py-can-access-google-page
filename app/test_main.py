from app import main
from app.main import can_access_google_page


def test_should_decline_if_no_internet(monkeypatch: object) -> None:
    def mocked_google_url(url: str) -> bool:
        return True

    def mocked_internet_connection() -> bool:
        return False

    monkeypatch.setattr(
        main,
        "valid_google_url",
        mocked_google_url
    )

    monkeypatch.setattr(
        main,
        "has_internet_connection",
        mocked_internet_connection
    )
    assert can_access_google_page("") == "Not accessible"


def test_should_decline_if_not_valid_url(monkeypatch: object) -> None:

    def mocked_google_url(url: str) -> bool:
        return False

    def mocked_internet_connection() -> bool:
        return True

    monkeypatch.setattr(
        main,
        "has_internet_connection",
        mocked_internet_connection
    )

    monkeypatch.setattr(
        main,
        "valid_google_url",
        mocked_google_url
    )
    assert can_access_google_page("") == "Not accessible"


def test_should_give_access_if_conditions_true(monkeypatch: object) -> None:
    def mocked_internet_connection() -> bool:
        return True

    def mocked_google_url(url: str) -> bool:
        return True

    monkeypatch.setattr(
        main,
        "has_internet_connection",
        mocked_internet_connection
    )
    monkeypatch.setattr(
        main,
        "valid_google_url",
        mocked_google_url
    )
    assert can_access_google_page("") == "Accessible"
