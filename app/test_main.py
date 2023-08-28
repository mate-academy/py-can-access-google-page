import pytest

from typing import Callable

from pytest import MonkeyPatch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, mock_valid_google_url, mock_internet_connection, expected_result",
    [
        pytest.param(
            "https://learn.microsoft.com",
            lambda url: True,
            lambda: True,
            "Accessible",
            id=("should return Accessible if"
                " valid_google_url and expected_result is True")
        ),
        pytest.param(
            "https://github.com",
            lambda url: False,
            lambda: True,
            "Not accessible",
            id="should return Not accessible if valid_google_url is False"
        ),
        pytest.param(
            "https://zoom.us",
            lambda url: True,
            lambda: False,
            "Not accessible",
            id="should return Not accessible if internet_connection is False"
        ),
        pytest.param(
            "https://mate.academy",
            lambda url: False,
            lambda: False,
            "Not accessible",
            id=("should return Not accessible if"
                " internet_connection and valid_google_url is False")
        ),
    ]
)
def test_check_access_google_page(
        url: str,
        monkeypatch: MonkeyPatch,
        mock_valid_google_url: Callable,
        mock_internet_connection: Callable,
        expected_result: str
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", mock_valid_google_url)
    monkeypatch.setattr("app.main.has_internet_connection",
                        mock_internet_connection)

    assert can_access_google_page(url) == expected_result
