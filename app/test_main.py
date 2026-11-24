import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_dependency() -> tuple[mock.MagicMock, mock.MagicMock]:
    with mock.patch("app.main.has_internet_connection") as connection:
        with mock.patch("app.main.valid_google_url") as url:
            yield connection, url


def test_can_access_google_page(
        mocked_dependency: tuple[mock.MagicMock, mock.MagicMock]
) -> None:
    connection, url = mocked_dependency
    can_access_google_page("https://www.google.com")
    connection.assert_called_once()
    url.assert_called_once_with("https://www.google.com")


@pytest.mark.parametrize(
    "internet_connection,valid_url,result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible")
    ]
)
def test_return_accessible_or_not(
        mocked_dependency: tuple[mock.MagicMock, mock.MagicMock],
        internet_connection: bool,
        valid_url: bool,
        result: str
) -> None:
    connection, url = mocked_dependency
    connection.return_value = internet_connection
    url.return_value = valid_url
    assert can_access_google_page("https://www.google.com") == result
