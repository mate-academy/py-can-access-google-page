import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, valid_url, expected_result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="should return Accessible, both conditions are True"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="should return Not accessible, only valid_url is True"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="should return Not accessible, only internet_connection is True"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="should return Not accessible because both conditions are False"
        ),
    ])
def test_can_access_google_page(
        internet_connection: bool,
        valid_url: bool,
        expected_result: str,
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: internet_connection
    )
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda url: valid_url
    )

    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == expected_result
