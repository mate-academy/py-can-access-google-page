from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize("connection, access, can_access",
                         [
                             (True, True, "Accessible"),
                             (True, False, "Not accessible"),
                             (False, True, "Not accessible")
                         ]
                         )
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_access(mocked_connection: mock,
                mocked_access: mock,
                connection: bool,
                access: bool,
                can_access: str
                ) -> None:
    mocked_connection.return_value = connection
    mocked_access.return_value = access
    assert can_access_google_page("google.com") == can_access
