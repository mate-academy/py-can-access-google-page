import pytest
from unittest.mock import MagicMock
import app.main as main
from app.main import can_access_google_page


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
    monkeypatch, is_valid, is_online, expected
) -> None:
    vmock = MagicMock(return_value=is_valid)
    imock = MagicMock(return_value=is_online)
    monkeypatch.setattr(main, "valid_google_url", vmock)
    monkeypatch.setattr(main, "has_internet_connection", imock)

    assert can_access_google_page("https://google.com") == expected


def test_can_access_google_page_calls_helpers_with_correct_args(
    monkeypatch,
) -> None:
    vmock = MagicMock(return_value=True)
    imock = MagicMock(return_value=True)
    monkeypatch.setattr(main, "valid_google_url", vmock)
    monkeypatch.setattr(main, "has_internet_connection", imock)

    url = "https://google.com"
    can_access_google_page(url)

    vmock.assert_called_once_with(url)
    imock.assert_called_once_with()
