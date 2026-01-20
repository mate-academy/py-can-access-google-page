import pytest
from _pytest.fixtures import SubRequest

from app import main


@pytest.fixture()
def mock_valid_google_url(request: SubRequest) -> callable:
    def _mock(url: str) -> bool:
        return request.param
    return _mock


@pytest.fixture()
def mock_has_internet_connection(request: SubRequest) -> callable:
    def _mock() -> bool:
        return request.param
    return _mock


@pytest.mark.parametrize(
    "mock_has_internet_connection, mock_valid_google_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    indirect=["mock_has_internet_connection", "mock_valid_google_url"]
)
def test_accessible_when_has_internet_and_valid_url(
        monkeypatch: callable,
        mock_has_internet_connection: callable,
        mock_valid_google_url: callable,
        expected: str
) -> None:
    monkeypatch.setattr(
        main, "valid_google_url", mock_valid_google_url
    )
    monkeypatch.setattr(
        main, "has_internet_connection", mock_has_internet_connection
    )

    assert main.can_access_google_page("some_url") == expected
