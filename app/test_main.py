import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_connection() -> None:
    with mock.patch(
        "app.main.has_internet_connection", return_value=False
    ):
        yield


def test_function_should_return_correct_response() -> None:
    assert (
        can_access_google_page("https://www.flashscore.com/")
        == "Accessible"
    )


def test_function_should_return_always_false(
    mocked_connection: mock.MagicMock,
) -> None:
    assert (
        can_access_google_page("https://www.flashscore.com/")
        == "Not accessible"
    )


@mock.patch("app.main.valid_google_url")
def test_valid_google_url(mock_url_validator: mock.MagicMock) -> None:
    can_access_google_page("https://www.flashscore.com/")
    mock_url_validator.assert_called_once()


@mock.patch("app.main.has_internet_connection")
def test_internet_connection(
    mocked_connection: mock.MagicMock,
) -> None:
    can_access_google_page("https://www.flashscore.com/")
    mocked_connection.assert_called_once()
