import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_net, is_valid, expected",
    [
        pytest.param(True, True, "Accessible",
                     id="has_net_and_valid_url"),
        pytest.param(True, False, "Not accessible",
                     id="has_net_but_invalid_url"),
        pytest.param(False, True, "Not accessible",
                     id="no_net_and_valid_url"),
        pytest.param(False, False, "Not accessible",
                     id="no_net_and_invalid_url"),
    ],
)
def test_can_access_google_page(
        has_net: bool,
        is_valid: bool,
        expected: str
) -> None:
    with patch("app.main.has_internet_connection", return_value=has_net):
        with patch("app.main.valid_google_url", return_value=is_valid):
            assert can_access_google_page("https://www.google.com/") == expected


def test_should_not_check_url_when_no_net() -> None:
    with (patch("app.main.has_internet_connection", return_value=False)):
        with patch("app.main.valid_google_url") as mock_valid:
            assert can_access_google_page(
                "https://www.google.com/"
            ) == "Not accessible"
            mock_valid.assert_not_called()


def test_should_check_url_when_valid_net() -> None:
    with patch("app.main.has_internet_connection", return_value=True):
        with patch("app.main.valid_google_url", return_value=True) as mock_valid:
            assert can_access_google_page("https://www.google.com/") == "Accessible"
            mock_valid.assert_called_once()
