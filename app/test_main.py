from _pytest.monkeypatch import MonkeyPatch

from app.main import can_access_google_page

import pytest


@pytest.mark.parametrize(
    "url_value, internet_value, expected_result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="valid_url_and_connection_exists",
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="valid_url_but_no_connection",
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="invalid_url_with_connection",
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="invalid_url_and_no_connection",
        ),
    ],
)
def test_can_access_google_page(
    monkeypatch: MonkeyPatch,
    url_value: bool,
    internet_value: bool,
    expected_result: str,
) -> None:

    monkeypatch.setattr("app.main.valid_google_url",
                        lambda url: url_value)
    monkeypatch.setattr("app.main.has_internet_connection",
                        lambda: internet_value)
    result = can_access_google_page("https://google.com")
    assert result == expected_result
