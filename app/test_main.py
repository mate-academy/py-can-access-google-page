from unittest import mock
import pytest


from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_return,connection_return,result",
    [
        pytest.param(True, True, "Accessible",
                     id="test_valid_google_url_True_and_"
                        "has_internet_connection_True_result_True"),
        pytest.param(True, False, "Not accessible",
                     id="test_valid_google_url_True_and_"
                        "has_internet_connection_False_result_False"),
        pytest.param(False, True, "Not accessible",
                     id="test_valid_google_url_False_and_"
                        "has_internet_connection_True_result_False"),
        pytest.param(False, False, "Not accessible",
                     id="test_valid_google_url_False_and_"
                        "has_internet_connection_False_result_False")
    ])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test__access_google_page(mock_connection: object,
                             mock_valid_url: object,
                             valid_google_return: bool,
                             connection_return: bool,
                             result: str) -> None:
    mock_connection.return_value = connection_return
    mock_valid_url.return_value = valid_google_return

    assert can_access_google_page(url="https://google.com") == result
