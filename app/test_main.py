from unittest.mock import Mock

import pytest

from app import main


@pytest.mark.parametrize(
    ("url_is_valid", "internet_is_available", "expected"),
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    url_is_valid: bool,
    internet_is_available: bool,
    expected: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    url = "https://www.google.com"
    valid_url_mock = Mock(return_value=url_is_valid)
    internet_mock = Mock(return_value=internet_is_available)
    monkeypatch.setattr(main, "valid_google_url", valid_url_mock)
    monkeypatch.setattr(main, "has_internet_connection", internet_mock)

    assert main.can_access_google_page(url) == expected

    internet_mock.assert_called_once_with()
    if internet_is_available:
        valid_url_mock.assert_called_once_with(url)
    else:
        valid_url_mock.assert_not_called()
