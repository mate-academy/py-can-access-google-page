import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.fixture()
def mocked_have_internet() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_have_internet:
        yield mock_have_internet


@pytest.mark.parametrize(
    "url_validation, check_internet, expected_result",
    [
        pytest.param(
            True, True, "Accessible",
            id="Accessible"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="Not accessible because no internet"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="Not accessible because of invalid url"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="Not accessible, invalid url and no internet"
        )
    ]
)
def test_can_access_google_page(mocked_valid_url: callable,
                                mocked_have_internet: callable,
                                url_validation: bool,
                                check_internet: bool,
                                expected_result: str) -> None:
    mocked_valid_url.return_value = url_validation
    mocked_have_internet.return_value = check_internet
    assert can_access_google_page("http://google.com") == expected_result
