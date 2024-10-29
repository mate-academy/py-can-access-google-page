from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


url = "https://google.com"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_with_mocked_different_dependencies(
        mocked_url: MagicMock,
        mocked_connection: MagicMock
) -> None:
    possible_variants = [
        [True, True],
        [True, False],
        [False, True],
        [False, False]
    ]
    for variant in possible_variants:
        mocked_url.return_value, mocked_connection.return_value = variant
        if all([mocked_url.return_value, mocked_connection.return_value]):
            assert can_access_google_page(url) == "Accessible"
        else:
            assert can_access_google_page(url) == "Not accessible"
