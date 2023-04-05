from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_accessible(mocked_connection: mock, mocked_access: mock) -> None:
    mocked_connection.return_value = True
    mocked_access.return_value = True
    assert can_access_google_page("google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_through_access(mocked_connection: mock,
                                       mocked_access: mock
                                       ) -> None:
    mocked_connection.return_value = True
    mocked_access.return_value = False
    assert can_access_google_page("google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_through_connection(mocked_connection: mock,
                                           mocked_access: mock
                                           ) -> None:
    mocked_connection.return_value = False
    mocked_access.return_value = True
    assert can_access_google_page("google.com") == "Not accessible"
