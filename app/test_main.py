from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_true_internet_true(
        mocked_internet: MagicMock,
        mocked_url: MagicMock
) -> None:
    mocked_internet.return_value = True
    mocked_url.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible"

    mocked_internet.assert_called_once()
    mocked_url.assert_called_once()


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_false_internet_true(mocked_internet: MagicMock,
                                 mocked_url: MagicMock
                                 ) -> None:
    mocked_internet.return_value = True
    mocked_url.return_value = False

    results = can_access_google_page("https://www.google.com")

    assert results == "Not accessible"

    mocked_internet.assert_called_once()
    mocked_url.assert_called_once()


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_true_internet_false(mocked_internet: MagicMock,
                                 mocked_url: MagicMock
                                 ) -> None:
    mocked_internet.return_value = False
    mocked_url.return_value = True

    results = can_access_google_page("https://www.google.com")

    assert results == "Not accessible"

    mocked_internet.assert_called_once()
    mocked_url.assert_not_called()


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_false_internet_false(mocked_internet: MagicMock,
                                  mocked_url: MagicMock
                                  ) -> None:
    mocked_internet.return_value = False
    mocked_url.return_value = False

    results = can_access_google_page("https://www.google.com")

    assert results == "Not accessible"

    mocked_internet.assert_called_once()
    mocked_url.assert_not_called()
