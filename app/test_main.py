import pytest
from unittest import mock

from app.main import can_access_google_page

@pytest.mark.parametrize(
		"valid_url, connection, expected",
		[
			(True, True, "Accessible"),
			(True, False, "Not accessible"),
			(False, True, "Not accessible"),
			(False, False, "Not accessible")
		],
)

def test_can_access_google_page(
								valid_url: bool,
								connection: bool,
								expected: str
								):
	with (mock.patch("app.main.valid_google_url") as \
		  mocked_valid_google_url, \
		  mock.patch("app.main.has_internet_connection") as \
		  mocked_has_internet_connection):
		mocked_valid_google_url.return_value = valid_url
		mocked_has_internet_connection.return_value = connection
		response = can_access_google_page("https://www.google.com")
		assert response == expected
