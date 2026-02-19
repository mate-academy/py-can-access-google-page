from unittest import mock


import app.main as main


def test_can_access_google_page() -> None:
    with (mock.patch("app.main.valid_google_url") as valid_google_url_for_test,
          mock.patch("app.main.has_internet_connection") as
          has_internet_connection_for_test):
        valid_google_url_for_test.return_value = True
        has_internet_connection_for_test.return_value = True
        assert (main.can_access_google_page("https://www.google.com")
                == "Accessible")


@mock.patch("app.main.valid_google_url")
def test_test_can_access_google_page_dont_connect_return_false(
        mock_for_test: bool) -> None:
    mock_for_test.return_value = False
    assert (main.can_access_google_page("https://www.google.com")
            == "Not accessible")


@mock.patch("app.main.has_internet_connection")
def test_test_can_access_google_page_without_internet_return_false(
        mock_for_test: bool) -> None:
    mock_for_test.return_value = False
    assert (main.can_access_google_page("https://www.google.com")
            == "Not accessible")
