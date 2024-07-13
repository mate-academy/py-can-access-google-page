from app.main import can_access_google_page
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "mocked_internet_return, mocked_valid_return, url, expected",
    [
        (
            True, True,
            (
                "https://www.google.com/"
                "webhp?hl=uk&sa=X&ved="
                "0ahUKEwidt-"
                "fAtJyHAxV4BdsEHaGQCtwQPAgI"
            ),
            "Accessible"
        ),
        (
            True, False,
            (
                "https://www.google.com/"
                "webhp?hl=uk&sa=X&ved="
                "0ahUKEwidt-"
                "fAtJyHAxV4BdsEHaGQCtwQPAgI"
            ),
            "Not accessible"
        ),
        (
            False, True,
            (
                "https://www.google.com/"
                "webhp?hl=uk&sa=X&ved="
                "0ahUKEwidt-"
                "fAtJyHAxV4BdsEHaGQCtwQPAgI"
            ),
            "Not accessible"
        ),
        (
            False, False,
            (
                "https://www.google.com/"
                "webhp?hl=uk&sa=X&ved="
                "0ahUKEwidt-"
                "fAtJyHAxV4BdsEHaGQCtwQPAgI"
            ),
            "Not accessible"
        ),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mocked_internet: any,
    mocked_valid: any,
    mocked_internet_return: bool,
    mocked_valid_return: bool,
    url: str,
    expected: str
) -> None:
    mocked_internet.return_value = mocked_internet_return
    mocked_valid.return_value = mocked_valid_return
    assert can_access_google_page(url) == expected
