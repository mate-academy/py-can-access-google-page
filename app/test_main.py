from unittest import mock
from unittest.mock import Mock

from app import main


@mock.patch("app.main.has_internet_connection")
def test_always_call_inet_connection_func_and_return_not_accessible_if_false(
    mock_inet_connection: Mock
) -> None:
    mock_inet_connection.return_value = False

    access_status = main.can_access_google_page("magic URL")

    mock_inet_connection.assert_called_once_with()
    assert access_status == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_call_valid_url_func_with_given_url_and_return_not_accessible_if_false(
        mock_inet_connection: Mock,
        mock_valid_url: Mock
) -> None:
    mock_inet_connection.return_value = True
    mock_valid_url.return_value = False

    access_status = main.can_access_google_page("magic URL")

    mock_valid_url.assert_called_once_with("magic URL")
    assert access_status == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_return_accessible_if_both_inner_funcs_returns_true(
    mock_inet_connection: Mock,
    mock_valid_url: Mock
) -> None:
    mock_inet_connection.return_value = True
    mock_valid_url.return_value = True

    access_status = main.can_access_google_page("magic URL")

    mock_valid_url.assert_called_once_with("magic URL")
    assert access_status == "Accessible"
