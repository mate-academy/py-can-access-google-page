from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_validation,internet_connection,result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="should be `Accessible` when all values are correct"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="should be `Not accessible` when no Internet connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="should be `Not accessible` when url is not valid"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="should be `Not accessible` when url not valid & no connection"
        )
    ]
)
def test_can_access_google_page(
        url_validation: bool,
        internet_connection: bool,
        result: str
) -> None:
    with (mock.patch("app.main.valid_google_url") as valid_google_url,
          mock.patch(
              "app.main.has_internet_connection") as has_internet_connection
          ):
        has_internet_connection.return_value = internet_connection
        valid_google_url.return_value = url_validation
        assert can_access_google_page("https://www.dckids.com/") == result
