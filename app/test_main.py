import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,has_internet,result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        valid_url: bool,
        has_internet: int,
        result: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mocked_valid_google_url,
        mock.patch("app.main.has_internet_connection") as mocked_has_internet
    ):
        mocked_valid_google_url.return_value = valid_url
        mocked_has_internet.return_value = has_internet
        assert can_access_google_page("google.com") == result
