import pytest
from pytest import MonkeyPatch


from app.main import can_access_google_page


@pytest.mark.parametrize("url,valid,connection,expected", [
    ("https://www.google.com", True, True, "Accessible"),
    ("https://www.google.com", True, False, "Not accessible"),
    ("https://www.google.com", False, True, "Not accessible"),
    ("https://www.google.com", False, False, "Not accessible")
])
def test_valid_url_and_connection_exists(monkeypatch: MonkeyPatch,
                                         url: str,
                                         expected: str,
                                         valid: bool,
                                         connection: bool
                                         ) -> None:
    with monkeypatch.context() as mocked:
        mocked.setattr("app.main.valid_google_url", lambda *args: valid)
        mocked.setattr("app.main.has_internet_connection",
                       lambda: connection)
        assert can_access_google_page("https://www.google.com") == expected
