import pytest
from pytest import MonkeyPatch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, has_internet_connection_value, expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="should return 'Accessible' if both value True"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="should return 'Not accessible' "
               "if has_internet_connection False"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="should return 'Not accessible' if is_valid_url False"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="should return 'Not accessible' if both value False"
        )
    ]
)
def test_can_access_google_page(
        is_valid_url: bool,
        has_internet_connection_value: bool,
        expected: str
) -> None:
    monkeypatch = MonkeyPatch()
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda *args: is_valid_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: has_internet_connection_value
    )
    assert can_access_google_page("") == expected
