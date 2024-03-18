import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize("mock_has_internet_connection_return, "
                         "mock_valid_google_url_return, "
                         "expected_result",
                         [
                             (True, True, "Accessible"),
                             (True, False, "Not accessible"),
                             (False, True, "Not accessible"),
                             (False, False, "Not accessible"),
                         ])
def test_can_access_google_page(mocker: callable,
                                mock_has_internet_connection_return: bool,
                                mock_valid_google_url_return: bool,
                                expected_result: str) -> None:
    mocker.patch("app.main.has_internet_connection",
                 return_value=mock_has_internet_connection_return)
    mocker.patch("app.main.valid_google_url",
                 return_value=mock_valid_google_url_return)

    result = can_access_google_page("https://www.google.com")
    assert result == expected_result
