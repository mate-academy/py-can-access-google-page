import pytest
from unittest import mock
from app.main import can_access_google_page

URL = "https://www.flashscore.com/"


@pytest.fixture()
def mock_internet() -> mock:
    with mock.patch(
        "app.main.has_internet_connection"
    ) as mocked_internet:
        yield mocked_internet


@pytest.fixture()
def mock_url() -> mock:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.mark.parametrize(
    "internet_status,url_status,expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
    ],
)
def test_can_access_google_page(
    mock_internet: mock,
    mock_url: mock,
    internet_status: bool,
    url_status: bool,
    expected_result: str,
) -> None:
    mock_internet.return_value = internet_status
    mock_url.return_value = url_status
    assert can_access_google_page(URL) == expected_result
