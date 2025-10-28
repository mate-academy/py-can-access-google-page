import pytest
from unittest.mock import Mock
import app.main as m


@pytest.mark.parametrize(
    ("is_valid_url", "has_internet", "expected"),
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "valid+online",
        "invalid+online",
        "valid+offline",
        "invalid+offline",
    ],
)
def test_can_access_google_page_returns_expected(
    is_valid_url: bool,
    has_internet: bool,
    expected: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:

    mock_valid = Mock(return_value=is_valid_url)
    mock_net = Mock(return_value=has_internet)

    monkeypatch.setattr(m, "valid_google_url", mock_valid)
    monkeypatch.setattr(m, "has_internet_connection", mock_net)

    url = "https://www.google.com"

    result = m.can_access_google_page(url)

    assert result == expected
    mock_net.assert_called_once_with()

    if has_internet:
        mock_valid.assert_called_once_with(url)
    else:
        mock_valid.assert_not_called()


def test_can_access_google_page_calls_in_order(
    monkeypatch: pytest.MonkeyPatch,
) -> None:

    calls = []

    def fake_internet() -> bool:
        calls.append("internet")
        return True

    def fake_valid(_: str) -> bool:
        calls.append("valid")
        return True

    monkeypatch.setattr(m, "has_internet_connection", fake_internet)
    monkeypatch.setattr(m, "valid_google_url", fake_valid)

    _ = m.can_access_google_page("https://www.google.com")

    assert calls == ["internet", "valid"], (
        "A ordem das chamadas deve ser: internet -> valid"
    )
