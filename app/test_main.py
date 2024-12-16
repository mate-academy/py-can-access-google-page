from unittest import mock


def test_can_access_google_page() -> None:
    with mock.patch("requests.get") as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200
