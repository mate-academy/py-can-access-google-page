import pytest
from unittest import mock


import app.main


@pytest.mark.parametrize(
    "valid_google_url_value,has_internet_connection_value,expectation",
    [
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Should test if the url is valid"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Should test if the we have internet connection"
        ),
        pytest.param(
            True,
            True,
            "Accessible",
            id="Should test if the url is valid"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="Should test both two functions"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page(
    mock_has_internet_connection: mock.MagicMock,
    mock_valid_google_url: mock.MagicMock,
    valid_google_url_value: bool,
    has_internet_connection_value: bool,
    expectation: str
) -> None:
    mock_valid_google_url.return_value = valid_google_url_value
    mock_has_internet_connection.return_value = has_internet_connection_value
    assert (
        app.main.can_access_google_page("https://www.google.com")
        == expectation
    )


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_internet_connection_called(
    mock_has_internet_connection: mock.MagicMock,
    mock_valid_google_url: mock.MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    app.main.can_access_google_page("https://www.google.com")
    mock_has_internet_connection.assert_called_once_with()


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_google_url_called(
    mock_valid_google_url: mock.MagicMock,
    mock_has_internet_connection: mock.MagicMock
) -> None:
    mock_has_internet_connection.return_value = True
    app.main.can_access_google_page("https://www.google.com")
    mock_valid_google_url.assert_called_once_with("https://www.google.com")
