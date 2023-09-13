from unittest import mock
import pytest

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "connection, url, result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="should return `Accessible` when all is ok"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="should return `Not accessible` when lost connection"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="should return `Not accessible` when url is false"
        )
    ]
)
def test_can_access_google_page(
        mocked_has_internet_connection: mock.MagicMock,
        mocked_valid_google_url: mock.MagicMock,
        connection: bool,
        url: bool,
        result: str
) -> None:

    mocked_has_internet_connection.return_value = connection
    mocked_valid_google_url.return_value = url

    assert can_access_google_page("https://www.google.com") == result
