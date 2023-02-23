from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection", result_value=True)
@mock.patch("app.main.valid_google_url", result_value=True)
def test_valid_url_and_has_internet_connection(
        mock_valid_url: mock,
        mock_has_connection: mock
) -> None:
    assert can_access_google_page(
        "https://mate.academy/learn?course=python"
    ) == "Accessible"


@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_valid_url_and_has_no_internet_connection(
        mock_valid_url: mock,
        mock_has_connection: mock
) -> None:
    assert can_access_google_page(
        "https://mate.academy/events/english-lesson"
    ) == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_invalid_url_and_has_no_internet_connection(
        mock_valid_url: mock,
        mock_has_connection: mock
) -> None:
    assert can_access_google_page(
        "https://www.wikipedia.org/"
    ) == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_invalid_url_and_has_internet_connection(
        mock_valid_url: mock,
        mock_has_connection: mock
) -> None:
    assert can_access_google_page(
        "https://www.youtube.com/"
    ) == "Not accessible"
