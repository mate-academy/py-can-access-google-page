from pytest_mock import MockerFixture

from app import main


def test_can_access_google_page_success(mocker: MockerFixture) -> None:
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=True)

    assert main.can_access_google_page("https://google.com") == "Accessible"


def test_can_access_google_page_invalid_url(
    mocker: MockerFixture,
) -> None:
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=True)

    assert (
        main.can_access_google_page("https://invalid-url.com")
        == "Not accessible"
    )


def test_can_access_google_page_no_internet(
    mocker: MockerFixture,
) -> None:
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=False)

    assert (
        main.can_access_google_page("https://google.com")
        == "Not accessible"
    )


def test_can_access_google_page_both_false(
    mocker: MockerFixture,
) -> None:
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=False)

    assert (
        main.can_access_google_page("https://invalid-url.com")
        == "Not accessible"
    )
