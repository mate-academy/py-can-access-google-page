import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet, is_url_valid, expected_response",
    [
        pytest.param(
            True, True, "Accessible",
            id="Has internet and url correct."
        ),
        pytest.param(
            True, False, "Not accessible",
            id="Has internet and url incorrect."
        ),
        pytest.param(
            False, True, "Not accessible",
            id="Has not internet and url correct."
        ),
        pytest.param(
            False, False, "Not accessible",
            id="Has not internet and url incorrect."
        )
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_has_internet_connection: mock.MagicMock,
        mocked_valid_google_url: mock.MagicMock,
        has_internet: bool,
        is_url_valid: bool,
        expected_response: str
) -> None:
    mocked_has_internet_connection.return_value = has_internet
    mocked_valid_google_url.return_value = is_url_valid

    assert can_access_google_page("https://www.google.com/")\
           == expected_response
