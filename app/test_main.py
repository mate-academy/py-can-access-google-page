import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock1_result,mock2_result,expected_result",
    [
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (True, True, "Accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_values(
        has_internet_connection: mock.MagicMock,
        valid_google_url: mock.MagicMock,
        mock1_result: bool,
        mock2_result: bool,
        expected_result: str
) -> None:
    has_internet_connection.return_value = mock1_result
    valid_google_url.return_value = mock2_result

    url = "https://"

    assert can_access_google_page(url) == expected_result

    has_internet_connection.assert_called_once()

    if mock1_result:
        valid_google_url.assert_called_once_with(url)
