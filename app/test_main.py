from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_accessible_when_url_is_valid_and_internet_exists(
    mocked_valid_url: mock.MagicMock,
    mocked_internet: mock.MagicMock,
) -> None:
    mocked_valid_url.return_value = True
    mocked_internet.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_when_url_is_invalid(
    mocked_valid_url: mock.MagicMock,
    mocked_internet: mock.MagicMock,
) -> None:
    mocked_valid_url.return_value = False
    mocked_internet.return_value = True

    result = can_access_google_page("https://example.com")

    assert result == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_when_internet_is_unavailable(
    mocked_valid_url: mock.MagicMock,
    mocked_internet: mock.MagicMock,
) -> None:
    mocked_valid_url.return_value = True
    mocked_internet.return_value = False

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_when_both_conditions_are_false(
    mocked_valid_url: mock.MagicMock,
    mocked_internet: mock.MagicMock,
) -> None:
    mocked_valid_url.return_value = False
    mocked_internet.return_value = False

    result = can_access_google_page("https://example.com")

    assert result == "Not accessible"
