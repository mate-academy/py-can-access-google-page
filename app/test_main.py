from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_when_true_false(mock_connection: mock,
                                                mock_valid: mock) -> None:
    mock_connection.return_value = True
    mock_valid.return_value = False
    url = "ccs.com"
    assert can_access_google_page(url) == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_when_false_true(mock_connection: mock,
                                                mock_valid: mock) -> None:
    mock_connection.return_value = False
    mock_valid.return_value = True
    url = "mate_academy.com"
    assert can_access_google_page(url) == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_when_all_true(mock_connection: mock,
                                              mock_valid: mock) -> None:
    mock_connection.return_value = True
    mock_valid.return_value = True
    url = "python.com"
    assert can_access_google_page(url) == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_all_false(mock_connection: mock,
                                          mock_valid: mock) -> None:
    mock_connection.return_value = False
    mock_valid.return_value = False
    url = "github.com"
    assert can_access_google_page(url) == "Not accessible"
