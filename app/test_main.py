import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "if_has_connection, if_url_is_valid, expected_result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
    ],
    ids=[
        "Should return 'Accessible' if connections and url are okey",
        "Should return 'Not accessible' if no Internet and url is invalid",
        "Should return 'Not accessible' if no Internet connection",
        "Should return 'Not accessible' if url is invalid",
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_for_accession_to_google_page(
        mocked_int_connection_check: mock,
        mocked_google_url_validation: mock,
        if_url_is_valid: bool,
        if_has_connection: bool,
        expected_result: str
) -> None:
    mocked_google_url_validation.return_value = if_url_is_valid
    mocked_int_connection_check.return_value = if_has_connection

    assert can_access_google_page("https://google.com/") == expected_result
