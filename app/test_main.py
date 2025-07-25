from app import main
from unittest import mock


@mock.patch("app.main.requests.get")
def test_valid_google_url(mock_get: object) -> None:
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response
    assert main.valid_google_url("google")


@mock.patch("app.main.datetime.datetime")
def test_has_internet_connection(mock_datetime: object) -> None:
    fake_now = mock.Mock()
    fake_now.hour = 7
    mock_datetime.now.return_value = fake_now
    assert main.has_internet_connection()


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_connection: object,
        mocked_url: object) -> None:

    mocked_connection.return_value = True
    mocked_url.return_value = True
    assert main.can_access_google_page("google") == "Accessible"
    mocked_connection.return_value = False
    mocked_url.return_value = True
    assert main.can_access_google_page("google") == "Not accessible"
    mocked_connection.return_value = True
    mocked_url.return_value = False
    assert main.can_access_google_page("google") == "Not accessible"


if __name__ == "__main__":
    pass
