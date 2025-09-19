from app.main import can_access_google_page


def test_valid_url_and_connection_returns_accessible(mocker: any) -> None:
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=True)
    assert can_access_google_page("google.com") == "Accessible"


def test_valid_url_and_no_connection_returns_not_accessible(mocker: any) -> None:
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=False)
    assert can_access_google_page("google.com") == "Not accessible"


def test_valid_url_and_connection_exists_with_all_false(mocker: any) -> None:
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=False)
    assert can_access_google_page("google.com") == "Not accessible"


def test_invalid_url_and_connection_returns_not_accessible(mocker: any) -> None:
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=True)
    assert can_access_google_page("google.com") == "Not accessible"
