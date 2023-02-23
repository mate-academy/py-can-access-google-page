import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "validator_value,connection_value,expected_result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "test should not access page if only 'connection' is True",
        "test should not access page if only 'valid url' is True",
        "test should not access page if 'connection' and 'valid_url' are False"
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_with_invalid_url(
        mocked_validator: mock,
        mocked_checker: mock,
        validator_value: bool,
        connection_value: bool,
        expected_result: str
) -> None:

    mocked_validator.return_value = validator_value
    mocked_checker.return_value = connection_value
    assert can_access_google_page("https://www.google.com") == expected_result
