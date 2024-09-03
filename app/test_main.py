from unittest import mock

from app.main import can_access_google_page


def test_function_return_correct_data() -> None:
    assert isinstance(can_access_google_page("https://www.google.com"), str)


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_url_and_internet(
    mock_val_url: bool, mock_int_con: bool
) -> None:
    mock_val_url.return_value = True
    mock_int_con.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_access_no_url_no_internet(
    mock_val_url: bool, mock_int_con: bool
) -> None:
    mock_val_url.return_value = False
    mock_int_con.return_value = False
    assert can_access_google_page("https://www.gle.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_access_no_url(
    mock_val_url: bool, mock_int_con: bool
) -> None:
    mock_val_url.return_value = False
    mock_int_con.return_value = True
    assert can_access_google_page("https://www.gle.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_access_no_internet(
    mock_val_url: bool, mock_int_con: bool
) -> None:
    mock_val_url.return_value = True
    mock_int_con.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
