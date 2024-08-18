from app.main import can_access_google_page

import pytest


@pytest.mark.parametrize(
    "url,expected_result",
    [
        pytest.param(
            "http://",
            "Not accessible",
            id=""
        ),
        pytest.param(
            "",
            "Not accessible",
            id="edge cases"
        ),
        pytest.param(
            "https://www.google.com.ua/?hl=uk",
            "Accessible",
            id="edge cases"
        ),
        pytest.param(
            "https://www.googles.com.ua/?hl=uk",
            "Not accessible",
            id="edge cases"
        ),
    ]
)
def test_all(url: str, expected_result: str) -> None:
    assert can_access_google_page(url) == expected_result
