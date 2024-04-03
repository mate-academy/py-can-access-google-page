import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection, valid_google_url, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        monkeypatch: None,
        has_internet_connection: bool,
        valid_google_url: bool,
        expected: str
) -> None:

    def mock_has_internet_connection(*args) -> bool:
        return has_internet_connection

    def mock_valid_google_url(*args) -> bool:
        return valid_google_url

    monkeypatch.setattr("app.main.has_internet_connection",
                        mock_has_internet_connection)
    monkeypatch.setattr("app.main.valid_google_url", mock_valid_google_url)

    address = "https://www.google.com"
    assert can_access_google_page(address) == expected
