from app.main import can_access_google_page


def test_valid_url_and_connection_exist(mocker):
    mock_valid = mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=True)
    assert can_access_google_page("some_url") == "Accessible"
    mock_valid.assert_called_once_with("some_url")


def test_valid_url_but_no_connection(mocker):
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=False)
    assert can_access_google_page("some_url") == "Not accessible"


def test_invalid_url_but_connection_exists(mocker):
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=True)
    assert can_access_google_page("some_url") == "Not accessible"


def test_invalid_url_and_no_connection(mocker):
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=False)
    assert can_access_google_page("some_url") == "Not accessible"
