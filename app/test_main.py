from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def valid_internet_page() -> str:
    return "https://www.google.com"


@pytest.fixture
def wrong_internet_page() -> str:
    return "https://www.Gwwosdfgle.caaam"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
# Success case
@pytest.mark.parametrize(
    "url, result",
    [
        ("https://www.google.com", True),
        ("https://uk-ua.facebook.com/", True),
        ("https://github.com/", True)
    ]
)
def test_can_access_google_page_success(
        mock_has_internet: mock.Mock,
        mock_valid_google_url: mock.Mock,
        url: str,
        result: bool
) -> None:
    mock_has_internet.return_value = True
    mock_valid_google_url.return_value = True
    result = can_access_google_page(url=url)
    assert result == "Accessible"
    mock_has_internet.assert_called_once()
    mock_valid_google_url.assert_called_once_with(url)


@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "url, result",
    [
        ("https://www.google.com", True),
        ("https://uk-ua.facebook.com/", True),
        ("https://github.com/", True)
    ]
)
def test_failed_internet_connection(mock_has_internet: mock.Mock,
                                    url: str,
                                    result: bool) -> None:
    mock_has_internet.return_value = False
    result = can_access_google_page(url)
    assert result == "Not accessible"
    mock_has_internet.assert_called_once()


@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "url, result",
    [
        ("https://www.Gogle.com", False),
        ("https://uk-ua.faaaCdebook.com/", False),
        ("https://GiThsdfub.com/", False)
    ]
)
def test_not_valid_url(mock_valid_google_url: mock.Mock,
                       url: str,
                       result: bool) -> None:
    mock_valid_google_url.return_value = False
    result = can_access_google_page(url)
    assert result == "Not accessible"
    mock_valid_google_url.assert_called_once_with(url)
