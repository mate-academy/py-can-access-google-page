from unittest import mock


from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_return_accessible_when_all_is_true(
        mocked_connection: bool,
        mocked_validation: bool
) -> None:
    mocked_connection.return_value = True
    mocked_validation.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_return_not_accessible_when_connection_is_false(
        mocked_connection: bool,
        mocked_validation: bool
) -> None:
    mocked_connection.return_value = False
    mocked_validation.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_return_not_accessible_when_validation_is_false(
        mocked_connection: bool,
        mocked_validation: bool
) -> None:
    mocked_connection.return_value = True
    mocked_validation.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_return_not_accessible_when_both_are_false(
        mocked_connection: bool,
        mocked_validation: bool
) -> None:
    mocked_connection.return_value = False
    mocked_validation.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
