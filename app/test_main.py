import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_valid,has_internet,google_url,expected_result",
    [
        pytest.param(
            True,
            True,
            "https://www.google.com/",
            "Accessible",
            id="Has internet and valid URL"
        ),
        pytest.param(
            False,
            True,
            "https://www.google/",
            "Not accessible",
            id="Has internet and invalid URL"
        ),
        pytest.param(
            True,
            False,
            "https://www.google.com/",
            "Not accessible",
            id="No internet and valid URL"
        ),
        pytest.param(
            False,
            False,
            "https://www.google/",
            "Not accessible",
            id="No internet and invalid URL"
        )
    ]
)
def test_can_access_google_page(
    url_valid: bool,
    has_internet: bool,
    google_url: str,
    expected_result: str,
) -> None:
    with (
        patch("app.main.valid_google_url", return_value=url_valid),
        patch("app.main.has_internet_connection", return_value=has_internet)
    ):
        assert can_access_google_page(google_url) == expected_result
