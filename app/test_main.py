from app.main import (valid_google_url, has_internet_connection,
                      can_access_google_page)

from unittest import mock


def test_should_return_true_for_google_url_func() -> None:
    with mock.patch("requests.get") as mocked_request:
        mocked_request.return_value.status_code = 200
        valid_google_url("http://google.com")
        mocked_request.assert_called_with("http://google.com")
    assert valid_google_url("http://google.com") is True


def test_should_return_true_for_internet_connection_func() -> None:
    with mock.patch("app.main.datetime") as mocked_datetime:
        mocked_datetime.datetime.now_return_value.hour = 10
        has_internet_connection()
    assert has_internet_connection() is True


def test_should_return_true_for_can_access_google_page() -> None:
    with (mock.patch("app.main.valid_google_url", return_value=True),
          mock.patch("app.main.has_internet_connection",
          return_value=False)):
        assert can_access_google_page("http://google.com") == "Not accessible"
