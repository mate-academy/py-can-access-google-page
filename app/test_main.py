import pytest
from pytest_mock import MockerFixture

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_connection_result, mock_url_result, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
        mocker: MockerFixture,
        mock_connection_result: bool,
        mock_url_result: bool,
        expected: str
) -> None:
    mock_has_internet = mocker.patch("app.main.has_internet_connection")
    mock_has_internet.return_value = mock_connection_result

    mock_requests_get = mocker.patch("app.main.requests.get")
    if mock_url_result:
        mock_requests_get.return_value.status_code = 200
    else:
        mock_requests_get.return_value.status_code = 404

    result = can_access_google_page("http://www.google.com")
    assert result == expected
