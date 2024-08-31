from unittest import mock
import pytest


from app.main import can_access_google_page


google_url = "https://www.google.com"


@pytest.mark.parametrize(
    "url,internet_connection,valid_url,result",
    [
        (google_url, True, False, "Not accessible"),
        (google_url, False, True, "Not accessible"),
        (google_url, False, False, "Not accessible"),
        (google_url, True, True, "Accessible")
    ]
)
def test_all_possible_values(url: str,
                             internet_connection: bool,
                             valid_url: bool,
                             result: str) -> None:
    with (mock.patch("app.main."
                     "has_internet_connection") as internet_verification,
          mock.patch("app.main.valid_google_url") as url_verification):
        internet_verification.return_value = internet_connection
        url_verification.return_value = valid_url
        assert can_access_google_page(url) == result
