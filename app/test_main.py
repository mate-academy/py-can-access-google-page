from typing import Iterator
import pytest
from app.main import can_access_google_page


def mock_valid_google_url(url: str) -> bool:
    print("mock_valid_google_url", url, url == "valid")
    return url == "valid"


def make_mock_has_internet_connection(hour: int) -> callable:
    def mock_has_internet_connection() -> bool:
        return 6 <= hour < 23

    return mock_has_internet_connection


@pytest.fixture(autouse=True)
def default_function_fixture(
        monkeypatch: pytest.MonkeyPatch
) -> Iterator[None]:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        mock_valid_google_url
    )
    yield
    monkeypatch.delattr("app.main.valid_google_url")


@pytest.mark.parametrize(
    "url,current_hours,expected_result",
    (
        ("valid", 12, "Accessible"),
        ("valid", 6, "Accessible"),
        ("valid", 22, "Accessible"),
        ("valid", 5, "Not accessible"),
        ("valid", 23, "Not accessible"),
        ("invalid", 12, "Not accessible"),
        ("invalid", 5, "Not accessible"),
    ),
    ids=(
        "should been `accessible` with hours in between limits",
        "should been `accessible` with hours in bottom limit",
        "should been `accessible` with hours in top limit",
        "should been `not accessible` with hours under bottom limit",
        "should been `not accessible` with hours up to top limit",
        "should been `not accessible` with invalid url and valid time",
        "should been `not accessible` with both invalid"
    )
)
def test_can_access_google_page(
        url: str,
        current_hours: int,
        expected_result: str,
        monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        make_mock_has_internet_connection(current_hours)
    )

    assert can_access_google_page(url) == expected_result
    monkeypatch.delattr("app.main.has_internet_connection")
