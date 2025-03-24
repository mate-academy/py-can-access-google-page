import app.main


def is_valid_google_url(url: str) -> bool:
    return True


def is_not_valid_google_url(url: str) -> bool:
    return False


def has_internet_connection() -> bool:
    return True


def no_internet_connection() -> bool:
    return False


def test_can_access_google_page(monkeypatch) -> None:
    monkeypatch.setattr(
        app.main,
        "valid_google_url",
        is_valid_google_url
    )

    monkeypatch.setattr(
        app.main,
        "has_internet_connection",
        has_internet_connection
    )

    assert (
        app.main.can_access_google_page("https://google.com")
        == "Accessible"
    )


def test_cant_access_google_page_only_valid_url(monkeypatch) -> None:
    monkeypatch.setattr(
        app.main,
        "valid_google_url",
        is_valid_google_url
    )

    monkeypatch.setattr(
        app.main,
        "has_internet_connection",
        no_internet_connection
    )

    assert (
        app.main.can_access_google_page("https://google.com")
        == "Not accessible"
    )


def test_cant_access_google_page_only_has_connection(monkeypatch) -> None:
    monkeypatch.setattr(
        app.main,
        "valid_google_url",
        is_not_valid_google_url
    )

    monkeypatch.setattr(
        app.main,
        "has_internet_connection",
        has_internet_connection
    )

    assert (
        app.main.can_access_google_page("https://google.com")
        == "Not accessible"
    )


def test_cant_access_google_page(monkeypatch) -> None:
    monkeypatch.setattr(
        app.main,
        "valid_google_url",
        is_not_valid_google_url
    )

    monkeypatch.setattr(
        app.main,
        "has_internet_connection",
        no_internet_connection
    )

    assert (
        app.main.can_access_google_page("https://google.com")
        == "Not accessible"
    )
