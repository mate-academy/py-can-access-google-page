import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


@pytest.mark.parametrize(
    "url_status, connection_status, access",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="should be accessible if url valid and has connection"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="should be not accessible if has no connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="should be not accessible if url is not valid"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="should be not accessible if url is not valid"
               "and has no connection"
        )
    ]
)
def test_can_access_google_page(
        url_status: bool,
        connection_status: bool,
        access: str,
        mocked_valid_google_url: pytest.fixture(),
        mocked_has_internet_connection: pytest.fixture()
) -> None:
    mocked_valid_google_url.return_value = url_status
    mocked_has_internet_connection.return_value = connection_status
    assert can_access_google_page("") == access
