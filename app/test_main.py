from app.main import can_access_google_page


def test_can_access_google_page(mocker: any) -> None:
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=True)
    assert can_access_google_page("google.com") == "Accessible"


def test_can_access_google_page_false1(mocker: any) -> None:
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=False)
    assert can_access_google_page("google.com") == "Not accessible"


def test_can_access_google_page_false2(mocker: any) -> None:
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=False)
    assert can_access_google_page("google.com") == "Not accessible"


def test_can_access_google_page_false3(mocker: any) -> None:
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=True)
    assert can_access_google_page("google.com") == "Not accessible"
