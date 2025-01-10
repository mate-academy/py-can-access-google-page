import pytest


from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_url, mock_internet, expected_result",
    [
        pytest.param(True, True, "Accessible",
                     id="URL is valid_there is access to the Internet"),
        pytest.param(False, True, "Not accessible",
                     id="not UPL and is access to the Internet"),
        pytest.param(False, False, "Not accessible",
                     id="not upl and internet"),
        pytest.param(True, False, "Not accessible",
                     id="not internet"),
    ]
)
def test_can_access_google_page(mocker, mock_url: bool,
                                mock_internet: bool,
                                expected_result: str) -> None:
    mocker.patch("app.main.valid_google_url", return_value=mock_url)
    mocker.patch("app.main.has_internet_connection", return_value=mock_internet)
    result = can_access_google_page("http://google.com")
    assert result == expected_result
