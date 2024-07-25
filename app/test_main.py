from app.main import can_access_google_page


from pytest import fixture
from unittest import mock
from unittest.mock import MagicMock


@fixture
def mock_valid() -> MagicMock:
    with mock.patch("app.main.valid_google_url") as mocked_valid:
        yield mocked_valid


@fixture
def mock_connection() -> MagicMock:
    with mock.patch("app.main.has_internet_connection") as mocked_connect:
        yield mocked_connect


def test_connection_and_valid_should_be_called(
        mock_valid: MagicMock,
        mock_connection: MagicMock
) -> None:
    can_access_google_page("http://customurl.co/homepage?session=abc")
    mock_valid.assert_called_once_with(
        "http://customurl.co/homepage?session=abc"
    )
    mock_connection.assert_called_once()


def test_cannot_be_access_if_valid_is_false(
        mock_valid: MagicMock,
        mock_connection: MagicMock
) -> None:
    mock_valid.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page("some url") == "Not accessible"


def test_cannot_be_access_if_connection_is_false(
        mock_valid: MagicMock,
        mock_connection: MagicMock
) -> None:
    mock_valid.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page("some url") == "Not accessible"


def test_cannot_access_if_all_functions_is_false(
        mock_valid: MagicMock,
        mock_connection: MagicMock
) -> None:
    mock_valid.return_value = False
    mock_connection.return_value = False
    assert can_access_google_page("some url") == "Not accessible"


def test_can_be_access_if_connection_and_valid_is_true(
        mock_valid: MagicMock,
        mock_connection: MagicMock
) -> None:
    mock_valid.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("some url") == "Accessible"
