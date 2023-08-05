import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize("internet_connection, google_url, expected_result", [
    pytest.param(True, True, "Accessible",
                 id="should return Accessible"),
    pytest.param(True, False, "Not accessible",
                 id="should return Not accessible"
                    " when google_url is False"),
    pytest.param(False, True, "Not accessible",
                 id="should return Not accessible "
                    "when internet connection is False"),
    pytest.param(False, False, "Not accessible",
                 id="should return Not accessible "
                    "when google_url and internet_connection is False")
])
def test_can_access_google_page(internet_connection: bool,
                                google_url: bool,
                                expected_result: str) -> None:
    with (
        mock.patch(
            "app.main.valid_google_url",
            return_value=google_url
        ),
        mock.patch(
            "app.main.has_internet_connection",
            return_value=internet_connection
        )
    ):
        result = can_access_google_page("https://www.google.com")
        assert result == expected_result
