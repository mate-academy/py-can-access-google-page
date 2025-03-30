import pytest
from typing import Any
import app.main
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "init_url, "
    "mocked_valid_google_url, "
    "mocked_has_internet_connection, "
    "expected_result",
    [
        pytest.param("https://www.google.pl/",
                     True,
                     True,
                     "Accessible",
                     id="valid url and connection is True"),
        pytest.param("https://www.google.pl/",
                     True,
                     False,
                     "Not accessible",
                     id="valid url is True and connection is False"),
        pytest.param("https://www",
                     False,
                     True,
                     "Not accessible",
                     id="valid url is False and connection is True"),
        pytest.param("https://www",
                     False,
                     False,
                     "Not accessible",
                     id="both are False"),
    ]
)
def test_can_access_google_page(monkeypatch: Any,
                                init_url: str,
                                mocked_valid_google_url: str,
                                mocked_has_internet_connection: bool,
                                expected_result: bool) -> None:

    def mock_valid_google_url(init_url: str) -> bool:
        return mocked_valid_google_url

    def mock_has_internet_connection() -> bool:
        return mocked_has_internet_connection

    monkeypatch.setattr(app.main,
                        "valid_google_url",
                        mock_valid_google_url)
    monkeypatch.setattr(app.main,
                        "has_internet_connection",
                        mock_has_internet_connection)
    result = can_access_google_page(init_url)
    assert result == expected_result
