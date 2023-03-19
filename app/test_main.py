from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_status, expected",
    [
        pytest.param(True, True, "Accessible",
                     id="Accessible, when all 'True'"),
        pytest.param(True, False, "Not accessible",
                     id="Not accessible, when valid_url is 'False'"),
        pytest.param(False, True, "Not accessible",
                     id="Not accessible, when internet_status is 'False'"),
        pytest.param(False, False, "Not accessible",
                     id="Not accessible, when all 'False'"),
    ]
)
def test_can_access_google_page(
        valid_url: bool,
        internet_status: bool,
        expected: str
) -> None:
    with mock.patch("app.main.valid_google_url",
                    return_value=valid_url):
        with mock.patch("app.main.has_internet_connection",
                        return_value=internet_status):
            assert can_access_google_page("ur.net") == expected
