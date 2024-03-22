import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url,has_internet_connection,expected_value",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Valid url and has internet",
        "Valid url but hasn't internet",
        "Invalid url but has internet",
        "Invalid url and hasn't internet",
    ]
)
def test_can_access_google_page(
        monkeypatch: object,
        valid_google_url: bool,
        has_internet_connection: bool,
        expected_value: str
) -> None:
    def mock_valid_google_url(_: None) -> bool:
        return valid_google_url

    def mock_has_internet_connection() -> bool:
        return has_internet_connection

    monkeypatch.setattr(
        "app.main.valid_google_url",
        mock_valid_google_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_has_internet_connection
    )
    assert can_access_google_page("https://www.google.com") == expected_value
