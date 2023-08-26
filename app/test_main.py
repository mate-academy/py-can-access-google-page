import pytest

from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_url, mock_internet, expected_result",
    [
        pytest.param(True, True, "Accessible", id="Access provided"),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Access denied due to lack of internet",
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Access denied due to unsatisfactory status code",
        ),
    ],
)
def test_can_access_google_page(
    mock_url: bool,
    mock_internet: bool,
    expected_result: str,
) -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_internet:
        with mock.patch("app.main.valid_google_url") as mocked_url:
            mocked_internet.return_value = mock_internet
            mocked_url.return_value = mock_url
            assert (
                can_access_google_page("https://www.google.com")
                == expected_result
            )
