import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url_result, has_connection_result, expected",
    [
        pytest.param(
            True,
            False,
            "Not accessible",
            id="cannot access if only connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="cannot access if only valid url"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_correctly_access(
        mocked_valid_url: mock.MagicMock,
        mocked_has_connection: mock.MagicMock,
        valid_url_result: bool,
        has_connection_result: bool,
        expected: str) -> None:
    mocked_valid_url.return_value = valid_url_result
    mocked_has_connection.return_value = has_connection_result
    assert can_access_google_page("https://google.com") == expected
