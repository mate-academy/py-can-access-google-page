from app.main import can_access_google_page

from pytest import mark

from unittest.mock import patch


@mark.parametrize(
    "url,has_internet_connection,expected_value",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "Parameters are correct.",
        "Parameter 'has_internet_connection' is not correct.",
        "Parameter 'url' is not correct.",
        "Parameters are not correct."
    ]
)
def test_can_access_google_page(url: bool,
                                has_internet_connection: bool,
                                expected_value: str) -> None:
    with (
        patch("app.main.valid_google_url") as mocked_valid_google_url,
        patch("app.main.has_internet_connection") as mocked_has_internet_con
    ):
        mocked_valid_google_url.return_value = url
        mocked_has_internet_con.return_value = has_internet_connection

        assert can_access_google_page("url") == expected_value
