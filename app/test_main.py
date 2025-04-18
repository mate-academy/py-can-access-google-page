import pytest

from app.main import can_access_google_page
from unittest import mock


@pytest.mark.parametrize(
    "bool_result_url, bool_result_has_internet, result",
     [
         (True, True, "Accessible"),
         (False, True, "Not accessible"),
         (True, False, "Not accessible"),
         (False, False, "Not accessible")
     ],
     ids=[
        "internet=True & url_accessible=True → Accessible",
        "internet=True & url_accessible=False → Not accessible",
        "internet=False & url_accessible=True → Not accessible",
        "internet=False & url_accessible=False → Not accessible"
     ]
)
def test_can_access_google_page(bool_result_url, bool_result_has_internet, result):
    with (mock.patch("app.main.valid_google_url", return_value=bool_result_url),
          mock.patch("app.main.has_internet_connection", return_value=bool_result_has_internet)):
        assert can_access_google_page("url") == result