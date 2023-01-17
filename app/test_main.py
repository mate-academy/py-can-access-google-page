from app.main import can_access_google_page
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "pages,valid_url,connection,result",
    [
        ("url", True, True, "Accessible"),
        ("url", True, False, "Not accessible"),
        ("url", False, True, "Not accessible")
    ]
)
def test_can_access_google_page(
        pages: str,
        valid_url: bool,
        connection: bool,
        result: str
) -> None:
    with mock.patch("app.main.valid_google_url") as valid:
        valid.return_value = valid_url
        with mock.patch("app.main.has_internet_connection") as request:
            request.return_value = connection
            assert can_access_google_page(pages) == result
