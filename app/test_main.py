from app.main import can_access_google_page


def test_valid_url_and_connection_returns_accessible(mocker: any) -> None:
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=True)
    assert can_access_google_page("google.com") == "Accessible"


def test_valid_url_and_connection_exists_with_first_false(mocker: any) -> None:
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=False)
    assert can_access_google_page("google.com") == "Not accessible"


def test_valid_url_and_connection_exists_with_oll_false(mocker: any) -> None:
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=False)
    assert can_access_google_page("google.com") == "Not accessible"


def test_valid_url_and_connection_exists_with_two_false(mocker: any) -> None:
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=True)
    assert can_access_google_page("google.com") == "Not accessible"
