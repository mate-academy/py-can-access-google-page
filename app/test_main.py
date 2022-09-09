import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "response, current_time, result", [
        pytest.param(
            True,
            True,
            "Accessible",
            id="test full access"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="test not valid internet"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="test not not access"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="test not valid internet and not access"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_url,
        mocked_connection,
        response,
        current_time,
        result
):
    mocked_url.return_value = response
    mocked_connection.return_value = current_time
    assert can_access_google_page("url") == result

# def test_full_access():
#     with mock.patch("app.main.valid_google_url") \
#             as mocked_url_func:
#         mocked_url_func.return_value = True
#
#         with mock.patch("app.main.has_internet_connection") \
#                 as mocked_internet_func:
#             mocked_internet_func.return_value = True
#
#             assert can_access_google_page("url") == "Accessible"
#
#
# def test_not_is_valid_url():
#     with mock.patch("app.main.valid_google_url") \
#             as mocked_url_func:
#         mocked_url_func.return_value = False
#
#         with mock.patch("app.main.has_internet_connection") \
#                 as mocked_internet_func:
#             mocked_internet_func.return_value = True
#
#             assert can_access_google_page("url") == "Not accessible"
#
#
# def test_not_connection_internet():
#     with mock.patch("app.main.valid_google_url") \
#             as mocked_url_func:
#         mocked_url_func.return_value = True
#
#         with mock.patch("app.main.has_internet_connection") \
#                 as mocked_internet_func:
#             mocked_internet_func.return_value = False
#
#             assert can_access_google_page("url") == "Not accessible"
