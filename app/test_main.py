from pytest import MonkeyPatch, mark


from app.main import can_access_google_page


@mark.parametrize(
    "url,url_validation,internet,result",
    [
        ("Not google url", False, True, "Not accessible"),
        ("Some google url", True, True, "Accessible"),
        ("Not google url", False, True, "Not accessible"),
        ("Some google url", True, True, "Accessible"),
        ("Not google url", False, False, "Not accessible"),
        ("Some google url", True, False, "Not accessible"),
    ],
    ids=[
        "Should return false when not google url",
        "Should return true when google url",
        "Should return false when not google url",
        "Should return true when google url",
        "Should return false when not google url, no internet",
        "Should return false when google url, no internet"
    ]
)
def test_can_access_google_page(url: str,
                                url_validation: bool,
                                internet: bool,
                                result: str,
                                monkeypatch: MonkeyPatch) -> None:

    monkeypatch.setattr("app.main.valid_google_url",
                        lambda *args: url_validation)
    monkeypatch.setattr("app.main.has_internet_connection",
                        lambda: internet)
    assert can_access_google_page(url) == result
