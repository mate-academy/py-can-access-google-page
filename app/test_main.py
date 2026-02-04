import pytest
import datetime
from unittest import mock
from unittest.mock import MagicMock
import app.main as main


@mock.patch("requests.get")
def test_valid_google_url(mock_get_response: MagicMock) -> None:
    main.valid_google_url("https://google.com")
    mock_get_response.assert_called_once_with("https://google.com")


def test_has_internet_connection() -> None:
    with mock.patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime.datetime(2020, 1, 1, 3, 0, 0)
        assert main.has_internet_connection() is False


@pytest.mark.parametrize(
    "valid_url, has_internet, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        monkeypatch: pytest.MonkeyPatch,
        valid_url: str,
        has_internet: bool,
        result: bool
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: valid_url)
    monkeypatch.setattr(main, "has_internet_connection", lambda: has_internet)
    assert main.can_access_google_page("any") == result
