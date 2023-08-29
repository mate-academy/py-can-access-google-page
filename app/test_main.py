import pytest
from pytest import MonkeyPatch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url_value,has_internet_connection_value,expected_result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="should return 'Accessible' when"
               " both functions return True",
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="should return 'Not accessible' when"
               " 'has_internet_connection' return False",
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="should return 'Not accessible' when"
               " 'valid_google_url_value' return False",
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="should return 'Not accessible' when"
               " both functions return False",
        ),
    ],
)
def test_can_access_google_page(
    monkeypatch: MonkeyPatch,
    valid_google_url_value: bool,
    has_internet_connection_value: bool,
    expected_result: str,
) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda url: valid_google_url_value
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: has_internet_connection_value,
    )

    assert can_access_google_page("") == expected_result

