import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_validator,connection_validator,result",
    [
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ]
)
def test_should_return_correct_result_with_difference_values(
        url_validator,
        connection_validator,
        result,
) -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_url_validator,
          mock.patch("app.main.has_internet_connection") as mocked_connection_validator):
        mocked_url_validator.return_value = url_validator
        mocked_connection_validator.return_value = connection_validator
        assert can_access_google_page("google.com") == result
