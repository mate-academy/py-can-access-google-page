import pytest
from unittest.mock import MagicMock
import app.main as main
from app.main import can_access_google_page
from _pytest.monkeypatch import MonkeyPatch


@pytest.mark.parametrize(
    "is_valid,is_online,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page_result(
    monkeypatch: "MonkeyPatch",
    is_valid: bool,
    is_online: bool,
    expected: str,
) -> None:
    monkeypatch.setattr(main, "valid_google_url", MagicMock(return_value=is_valid))
    monkeypatch.setattr(main, "has_internet_connection", MagicMock(return_value=is_online))

    assert can_access_google_page("https://google.com") == expected


def test_can_access_google_page_calls_helpers_with_correct_args(
    monkeypatch: "MonkeyPatch",
) -> None:
    vmock: MagicMock = MagicMock(return_value=True)
    imock: MagicMock = MagicMock(return_value=True)
    monkeypatch.setattr(main, "valid_google_url", vmock)
    monkeypatch.setattr(main, "has_internet_connection", imock)

    url = "https://google.com"
    can_access_google_page(url)

    vmock.assert_called_once_with(url)
    imock.assert_called_once_with()
