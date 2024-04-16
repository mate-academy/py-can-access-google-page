import pytest

from app.main import can_access_google_page
from unittest import mock


@pytest.mark.parametrize(
    "fake_url,fake_connection,result",
    [
        pytest.param(True, True, "Accessible"),
        pytest.param(True, False, "Not accessible"),
        pytest.param(False, True, "Not accessible"),
        pytest.param(False, False, "Not accessible")
    ],
    ids=[
        "when both funcs are true",
        "when first func is true, second is false",
        "when first func is false, second is true",
        "when both funcs are false",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mocked_url: mock.MagicMock,
    mocked_connection: mock.MagicMock,
    fake_url: bool,
    fake_connection: bool,
    result: str
) -> None:
    mocked_url.return_value = fake_url
    mocked_connection.return_value = fake_connection
    assert can_access_google_page("any_web_site") == result
