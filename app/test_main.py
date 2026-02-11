from unittest import mock


def test_valid_url() -> None:
    with mock.patch("app.main.valid_google_url",
                    return_value=True) as mocked_valid_google_url:
        assert mocked_valid_google_url()


def test_has_internet_connection() -> None:
    with (mock.patch("app.main.has_internet_connection") as
          mocked_has_internet_connection):
        assert mocked_has_internet_connection()


def test_should_access_google_page() -> None:
    with (mock.patch("app.main.can_access_google_connectioin") as
          mocked_can_access_google_connection):
        result = mocked_can_access_google_connection("https://www.google.com/")
        assert result == "Accessible"
