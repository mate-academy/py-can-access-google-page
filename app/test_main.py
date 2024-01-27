from app.main import can_access_google_page
from unittest import mock


def test_check_data_input() -> None:
    assert (
        can_access_google_page("https://www.google.com/") == "Accessible"
    )


@mock.patch("app.main.valid_google_url")
def test_url_function_execution(valid: mock) -> None:
    can_access_google_page("https://www.google.com")
    valid.asser_celled_onece()


@mock.patch("app.main.can_access_google_page")
def test_access_function_execution(access: mock) -> None:
    print(type(access))
    can_access_google_page("https://www.google.com")
    access.asser_celled_onece()
