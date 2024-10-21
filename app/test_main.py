from pytest_mock import MockerFixture
from app.main import can_access_google_page


def mock_functions(mocker: MockerFixture,
                   valid_url: bool,
                   has_internet: bool) -> None:
    mocker.patch("app.main.valid_google_url", return_value=valid_url)
    mocker.patch("app.main.has_internet_connection", return_value=has_internet)


def test_accessible_page(mocker: MockerFixture) -> None:
    mock_functions(mocker, valid_url=True, has_internet=True)

    result = can_access_google_page("url")
    assert result == "Accessible"


def test_not_accessible_due_to_invalid_url(mocker: MockerFixture) -> None:
    mock_functions(mocker, valid_url=False, has_internet=True)

    result = can_access_google_page("url")
    assert result == "Not accessible"


def test_not_accessible_due_to_no_internet(mocker: MockerFixture) -> None:
    mock_functions(mocker, valid_url=True, has_internet=False)

    result = can_access_google_page("url")
    assert result == "Not accessible"
