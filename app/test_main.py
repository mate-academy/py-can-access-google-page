import pytest
from pytest import MonkeyPatch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url,has_internet_connection,expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="should return 'Accessible' when both function return 'True'"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="should return 'Not accessible' "
               "when 'valid_google_url' return 'False'"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="should return 'Not accessible' "
               "when 'has_internet_connection' return 'False'"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="should return 'Not accessible' "
               "when both function return 'False'"
        ),
    ]
)
def test_can_access_google_page(
        monkeypatch: MonkeyPatch,
        valid_google_url: bool,
        has_internet_connection: bool,
        expected: str
) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda *args: valid_google_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda *args: has_internet_connection
    )
    assert can_access_google_page("") == expected
