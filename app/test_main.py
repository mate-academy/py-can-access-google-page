import pytest
from app.main import can_access_google_page
from unittest import mock


@pytest.mark.parametrize(
    "url, has_internet,valid_url,result",
    [
        pytest.param(
            "google.com",
            True,
            True,
            "Accessible"
        ),
        pytest.param(
            "googlsdfasdfe.com",
            True,
            False,
            "Not accessible"
        ),
        pytest.param(
            "google.com",
            False,
            True,
            "Not accessible"
        ),
        pytest.param(
            "googfdfgdfgle.com",
            False,
            False,
            "Not accessible"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_connection,
        mocked_url,
        url,
        has_internet,
        valid_url,
        result
):
    mocked_connection.return_value = has_internet
    mocked_url.return_value = valid_url
    assert can_access_google_page(url) == result
