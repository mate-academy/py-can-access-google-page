from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet: mock,
                                mock_valid_google_url: mock) -> None:
    mock_has_internet.side_effect = [True, False, True]
    mock_valid_google_url.side_effect = [False, True, True]
    answers = ["Not accessible", "Not accessible", "Accessible"]
    for answer in answers:
        assert can_access_google_page("some url") == answer
