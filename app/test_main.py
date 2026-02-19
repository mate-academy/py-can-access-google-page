from unittest import mock


import app.main as main


def test_can_access_google_page() -> None:
    assert (main.can_access_google_page("https://www.google.com")
            == "Accessible")


@mock.patch("app.main.valid_google_url")
def test_test_can_access_google_page_with_false(mock_for_test: bool) -> None:
    mock_for_test.return_value = False
    assert (main.can_access_google_page("https://www.google.com")
            == "Not accessible")


@mock.patch("app.main.has_internet_connection")
def test_test_can_access_google_page_with_false2(mock_for_test: bool) -> None:
    mock_for_test.return_value = False
    assert (main.can_access_google_page("https://www.google.com")
            == "Not accessible")
