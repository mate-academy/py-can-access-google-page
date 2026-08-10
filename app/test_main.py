import pytest

from unittest import mock

from app import main


@mock.patch("requests.get")
def test_valid_google_url(mock_get: mock.Mock) -> None:
    mock_get.return_value.status_code = 200
    assert main.valid_google_url("https://google.com") is True

def test_has_internet_connection(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.requests.get", mock.Mock())
    assert main.has_internet_connection() is True


@pytest.mark.parametrize(
    "has_connection, is_valid_url, expected_result",
    [
        pytest.param(
            True, True, "Accessible",
            id="connection and valid url"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="no connection"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="valid url"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="no connection and valid url"
        ),
    ]
)
def test_can_access_google_page_with_mocked_requests(
        monkeypatch: pytest.MonkeyPatch,
        has_connection: bool,
        is_valid_url: bool,
        expected_result: str
) -> None:
    url = "https://google.com" if is_valid_url else "https://ya.ru"
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: has_connection
    )
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda x: is_valid_url
    )
    assert main.can_access_google_page(url) == expected_result
