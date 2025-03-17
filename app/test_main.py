import unittest
from unittest.mock import patch, Mock

import random
from app.main import can_access_google_page


@patch("requests.get")
@patch("datetime.datetime.now")
def test_can_access_google_page(mock_get: any, mock_time: any) -> None:
    mock_time.return_value.hour = random.randint(6, 23)

    mock_response = Mock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    result = can_access_google_page("google.com")

    assert result is True


if __name__ == "__main__":
    unittest.main()
