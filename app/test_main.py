from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_is_valid,has_internet,expected",
    [
        pytest.param(
            True, True, "Accessible",
            id="valid url and internet available -> Accessible",
        ),
        pytest.param(
            True, False, "Not accessible",
            id="valid url but no internet -> Not accessible",
        ),
        pytest.param(
            False, True, "Not accessible",
            id="invalid url but internet available -> Not accessible",
        ),
        pytest.param(
            False, False, "Not accessible",
            id="invalid url and no internet -> Not accessible",
        ),
    ],
)
def test_can_access_google_page(
        url_is_valid: bool,
        has_internet: bool,
        expected: str,
) -> None:
    with (
        mock.patch(
            "app.main.valid_google_url",
            return_value=url_is_valid,
        ),
        mock.patch(
            "app.main.has_internet_connection",
            return_value=has_internet,
        ),
    ):
        assert can_access_google_page("https://www.google.com") == expected
