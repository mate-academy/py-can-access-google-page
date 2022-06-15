from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize("validation, connection, expected_output",
                         [
                             pytest.param(True, True, "Accessible",
                                          id="access if valid url &"
                                             " connected"),
                             pytest.param(False, True, "Not accessible",
                                          id="denied if url not valid"),
                             pytest.param(True, False, "Not accessible",
                                          id="denied if unconnected")
                         ]
                         )
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_validation,
                                mocked_connection,
                                validation,
                                connection,
                                expected_output):
    mocked_validation.return_value = validation
    mocked_connection.return_value = connection
    assert can_access_google_page(mocked_validation) == expected_output
