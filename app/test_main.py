import pytest

from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "status_code, econnect_bool, expected_result",
    (
        pytest.param(
            200,
            True,
            "Accessible",
            id="if code is 200 and have access to internet",
        ),
        pytest.param(
            200,
            False,
            "Not accessible",
            id="if code is 200 and don't have access to internet",
        ),
        pytest.param(404, True, "Not accessible", id="if wrong status code"),
    ),
)
def test_can_access_google_page(
    status_code: int, econnect_bool: bool, expected_result: str
) -> None:
    with patch("requests.get") as response_mock, patch(
        "app.main.has_internet_connection"
    ) as mock_has_internet_connection:
        response_mock.return_value.status_code = status_code
        mock_has_internet_connection.return_value = econnect_bool
        assert can_access_google_page("https://google.com") == expected_result
