import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet,valid_url,result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Accessible if url and connection valid"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Not accessible if no internet connection"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Not accessible if url is not valid"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="Not accessible if no connection and no valid url"
        ),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_valid_url,
        mocked_has_internet,
        internet,
        valid_url,
        result,
):
    mocked_has_internet.return_value = internet
    mocked_valid_url.return_value = valid_url

    response = can_access_google_page('')

    assert response == result
