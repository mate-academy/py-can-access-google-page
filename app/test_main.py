from unittest import mock
from app.main import can_access_google_page


def test_function_return_correct_type_of_data() -> None:
    assert isinstance(can_access_google_page("https://www.google.com"), str)


@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(mocked_internet: mock) -> None:
    mocked_internet.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"
    mocked_internet.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
    mocked_internet.return_value = True
    with mock.patch("app.main.valid_google_url") as mock_url:
        mock_url.return_value = True
        assert can_access_google_page("url") == "Accessible"
        mock_url.return_value = False
        assert can_access_google_page("url") == "Not accessible"
