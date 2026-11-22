from unittest import mock
import pytest


from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url_result, "
    "has_internet_connection_result, "
    "expected_result", [
        pytest.param(True,
                     True,
                     "Accessible",
                     id="Valid url and internet connection."),
        pytest.param(False,
                     True,
                     "Not accessible",
                     id="Invalid url and internet connection."),
        pytest.param(True,
                     False,
                     "Not accessible",
                     id="Valid url without internet connection."),
        pytest.param(False,
                     False,
                     "Not accessible",
                     id="Invalid url without internet connection.")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_internet_check: mock.Mock,
        mocked_url_check: mock.Mock,
        valid_google_url_result: bool,
        has_internet_connection_result: bool,
        expected_result: str
) -> None:
    mocked_internet_check.return_value = valid_google_url_result
    mocked_url_check.return_value = has_internet_connection_result
    assert can_access_google_page("") == expected_result
