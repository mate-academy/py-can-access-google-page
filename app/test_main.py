import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_url_valid, is_internet_connection, expected_result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Accessible if the URL is valid and there is an internet"
               "connection."
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Not accessible if the URL is valid, but there is no internet"
               "connection."
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Not accessible if the URL is invalid, but there is an internet"
               "connection."
        ),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_url: mock,
        mocked_internet_connection: mock,
        is_url_valid: bool,
        is_internet_connection: bool,
        expected_result: str
) -> None:
    mocked_valid_url.return_value = is_url_valid
    mocked_internet_connection.return_value = is_internet_connection
    assert can_access_google_page(
        "https://www.google.com"
    ) == expected_result
