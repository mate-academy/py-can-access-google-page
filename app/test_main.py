import pytest
from app import main


@pytest.mark.parametrize(
    "valid_param,internet_param,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "valid url and internet connection",
        "valid google url and no internet connection",
        "not valid google url and internet connection",
        "not valid google url and no internet connection"
    ]
)
def test_can_access_google_page(valid_param: bool,
                                internet_param: bool,
                                expected: bool,
                                monkeypatch: pytest.MonkeyPatch) -> None:

    monkeypatch.setattr(main, "valid_google_url", lambda url: valid_param)
    monkeypatch.setattr(main,
                        "has_internet_connection",
                        lambda: internet_param)
    result = main.can_access_google_page("https://google.com")
    assert result == expected
