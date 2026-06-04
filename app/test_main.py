import pytest
from app.main import valid_google_url, has_internet_connection 
from app.main import can_access_google_page


def test_an_access_google_page():
    assert can_access_google_page("https://www.google.com/") == "Accessible"

# def test_an_access_google_page2():
#     with pytest.raises(ConnectionError, match="Not accessible"):
#         can_access_google_page("https://www.google.comm/")