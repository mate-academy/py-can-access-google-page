import pytest

from app import main


def test_cannot_access_if_connection_or_valid_url_is_true(monkeypatch):
    def can_access_if_connection_or_valid_url(url):
        from app.main import has_internet_connection, valid_google_url

        if has_internet_connection() or valid_google_url(url):
            return "Accessible"
        else:
            return "Not accessible"

    monkeypatch.setattr(
        main, "can_access_google_page", can_access_if_connection_or_valid_url
    )

    test_result = pytest.main(["app/test_main.py"])
    assert test_result.value == 1, (
        "You cannot access page if only one of 'connection' or " "'valid url' is True."
    )


def test_cannot_access_if_only_connection(monkeypatch):
    def can_access_if_connection(url):
        from app.main import has_internet_connection, valid_google_url

        if has_internet_connection():
            return "Accessible"
        else:
            return "Not accessible"

    monkeypatch.setattr(main, "can_access_google_page", can_access_if_connection)

    test_result = pytest.main(["app/test_main.py"])
    assert (
        test_result.value == 1
    ), "You cannot access page if only 'connection' is True."


def test_cannot_access_if_only_valid_url(monkeypatch):
    def can_access_if_connection(url):
        from app.main import has_internet_connection, valid_google_url

        if valid_google_url(url):
            return "Accessible"
        else:
            return "Not accessible"

    monkeypatch.setattr(main, "can_access_google_page", can_access_if_connection)

    test_result = pytest.main(["app/test_main.py"])
    assert test_result.value == 1, "You cannot access page if only 'valid url' is True."
