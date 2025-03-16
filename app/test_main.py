# write your code here
import datetime
import responses
import pytest
from unittest.mock import patch
from app.main import can_access_google_page, you_have_to_give_me_mocked_datetime


@patch("app.main.datetime.date")
def test_mocked_datetime(mocked_date):
    mocked_date.today.return_value = datetime.date(2025, 3, 17)
    assert you_have_to_give_me_mocked_datetime() == datetime.date(2025, 3, 17)

# ----------------------------------------------------------------------

@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_both(mocked_google, mocked_connection):
    mocked_google.return_value = True
    mocked_connection.return_value = True

    assert can_access_google_page(url="https://www.google.com/") == "Accessible"


# ----------------------------------------------------------------------


@pytest.fixture
def mock_google_response():
    with patch("app.main.valid_google_url") as google_resp:
        yield google_resp


@pytest.fixture
def mock_internet_connection():
    with patch("app.main.has_internet_connection") as internet_conn:
        yield internet_conn


def test_cannot_access_both(mock_google_response, mock_internet_connection):
    mock_google_response.return_value = False
    mock_internet_connection.return_value = False

    assert can_access_google_page(url="https://www.google.com/") == "Not accessible"



# ----------------------------------------------------------------------


@pytest.fixture
def mock_can_access():
    with patch("app.main.valid_google_url") as google_resp, patch("app.main.has_internet_connection") as internet_conn:
        yield google_resp, internet_conn


def test_no_internet_connection(mock_can_access):
    google_resp, internet_conn = mock_can_access
    google_resp.return_value = True
    internet_conn.return_value = False

    assert can_access_google_page(url="https://www.google.com/") == "Not accessible"


# ----------------------------------------------------------------------

@pytest.fixture
def rsps():
    with responses.RequestsMock() as rsps:
        yield rsps


@pytest.fixture
def mock_internet_connection():
    with patch("app.main.has_internet_connection") as internet_conn:
        internet_conn.return_value = True
        yield internet_conn


def test_invalid_google_response(rsps, mock_internet_connection):
    rsps.get(
        url="https://www.google.com/",
        status=404,
    )

    assert can_access_google_page(url="https://www.google.com/") == "Not accessible"




# ------------------------IMO BEST SOLUTION----------------------------------

@pytest.fixture
def rsps():
    with responses.RequestsMock() as rsps:
        yield rsps


@pytest.fixture
def google_url():
    return "https://www.google.com/"


@pytest.fixture
def mock_google_response(rsps, google_url):
    def _mock_google_response(status_code):
        rsps.get(
            url=google_url,
            status=status_code,
        )
    return _mock_google_response


@pytest.fixture
def mock_internet_connection():
    with patch("app.main.has_internet_connection") as internet_conn:
        yield internet_conn


@pytest.mark.parametrize("google_status_code, is_internet_connection, expected_result",
    [
        (200, True, "Accessible"),
        (404, True, "Not accessible"),
        (200, False, "Not accessible"),
        (404, False, "Not accessible")
    ],
    ids=["all_success", "google_404", "no_internet", "both_fails"]
)
def test_all_possible_cases(
    mock_google_response, 
    mock_internet_connection,
    google_status_code, 
    is_internet_connection, 
    expected_result,
):
    if is_internet_connection:
        mock_google_response(status_code=google_status_code)
    mock_internet_connection.return_value = is_internet_connection

    assert can_access_google_page(url="https://www.google.com/") == expected_result