import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,connection,result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        url: bool,
        connection: bool,
        result: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mocked_url,
        mock.patch("app.main.has_internet_connection") as mocked_connection
    ):
        mocked_url.return_value = url
        mocked_connection.return_value = connection
        assert can_access_google_page("passed_url") == result
