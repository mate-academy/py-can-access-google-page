import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_url_valid,mock_internet,result_value",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Valid url and connection"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Valid url and invalid connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Invalid url and valid connection"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="Invalid url and invalid connection"
        ),
    ]
)
def test_can_access_google_page(
        mock_url_valid: bool,
        mock_internet: bool,
        result_value: str
) -> None:
    with (
        patch("app.main.has_internet_connection", return_value=mock_internet),
        patch("app.main.valid_google_url", return_value=mock_url_valid)
    ):
        assert can_access_google_page("https://www.google.com") == result_value
