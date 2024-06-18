from unittest import mock
from typing import Callable

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
	"return_valid, return_internet_connection, result",
	[
		(True, True, "Accessible"),
		(True, False, "Not accessible"),
		(False, True, "Not accessible"),
		(False, False, "Not accessible")
	]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_function_can_access_google_page(
		mock_valid_google_url: Callable,
		mock_has_internet_connection: Callable,
		return_valid: bool,
		return_internet_connection: bool,
		result: str
) -> None:
	mock_has_internet_connection.return_value = return_internet_connection
	mock_valid_google_url.return_value = return_valid
	assert can_access_google_page("https://google.com") == result
