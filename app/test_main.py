from unittest import mock
from .main import can_access_google_page
import pytest


@pytest.fixture()
def mocked_has_internet_connection() -> mock:
    with mock.patch(
        "app.main.has_internet_connection"
    ) as mocked_internet:
        yield mocked_internet


@pytest.fixture()
def mocked_valid_google_url() -> mock:
    with mock.patch(
            "app.main.valid_google_url"
    ) as mocked_url:
        yield mocked_url


@pytest.mark.parametrize(
    "validation_google_url,"
    " checking_has_internet_connection,"
    " return_can_access_page",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_google_url: mock,
        mocked_has_internet_connection: bool,
        validation_google_url: bool,
        checking_has_internet_connection: bool,
        return_can_access_page: str
) -> None:
    mocked_valid_google_url.return_value = validation_google_url
    mocked_has_internet_connection.return_value = (
        checking_has_internet_connection
    )
    assert (can_access_google_page("https://www.google.com")
            == return_can_access_page)
