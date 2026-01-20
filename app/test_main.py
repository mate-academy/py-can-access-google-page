from unittest import mock
import pytest


from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url():
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mocked_has_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mock_internet:
        yield mock_internet


@pytest.mark.parametrize(
    "has_internet, url, result",
    [
        pytest.param(True, True, "Accessible", id="you can visit site"),
        pytest.param(True, False, "Not accessible", id="incorrect url"),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="incorrect url and no internet access"
        ),
        pytest.param(False, True, "Not accessible", id="no internet access"),
    ]
)
def test_can_access_google_page(
        has_internet,
        url,
        result,
        mocked_valid_url,
        mocked_has_internet_connection

):
    mocked_valid_url.return_value = url
    mocked_has_internet_connection.return_value = has_internet
    assert can_access_google_page(mocked_valid_url) == result
