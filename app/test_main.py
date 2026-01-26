import pytest
from unittest.mock import Mock
from app import main


@pytest.mark.parametrize(
    "internet_ok,url_ok,expected,valid_called",
    [
        (True, True, "Accessible", True),
        (True, False, "Not accessible", True),
        (False, True, "Not accessible", False),
        (False, False, "Not accessible", False),
    ],
)
def test_can_access_google_page(
    monkeypatch: pytest.MonkeyPatch,
    internet_ok: bool,
    url_ok: bool,
    expected: str,
    valid_called: bool,
) -> None:
    # Mock de has_internet_conection
    monkeypatch.setattr(main, "has_internet_connection", lambda: internet_ok)

    # Mock espía de valid_google_url
    valid_mock = Mock(return_value=url_ok)
    monkeypatch.setattr(main, "valid_google_url", valid_mock)

    result = main.can_access_google_page("https://www.google.com")
    assert result == expected

    if valid_called:
        valid_mock.assert_called_once_with("https://www.google.com")
    else:
        valid_mock.assert_not_called()
