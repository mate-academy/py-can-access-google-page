from unittest import mock
import pytest


from app.main import can_access_google_page, valid_google_url, has_internet_connection


@pytest.fixture()
def mocked_valid_google_url():
    with mock.patch('app.main.valid_google_url') as mocked:
        yield mocked


@pytest.fixture()
def mocked_has_internet_connection():
    with mock.patch('app.main.has_internet_connection') as mocked:
        yield mocked


@pytest.mark.parametrize(
    "is_valid_url_status, internet_connection_status, awaited_result",
    [
        pytest.param(
            False,
            False,
            'Not accessible',
            id='Not accessible when is no connection and url not valid'
        ),
        pytest.param(
            False,
            True,
            'Not accessible',
            id='Not accessible when not valid url'
        ),
        pytest.param(
            True,
            False,
            'Not accessible',
            id='Not when where is no connection'
        ),
        pytest.param(
            True,
            True,
            'Accessible',
            id='Accessible when connection is ok and url is valid'
        ),
    ]
)
def test_can_access_google_page(
        mocked_valid_google_url,
        mocked_has_internet_connection,
        is_valid_url_status,
        internet_connection_status,
        awaited_result
):
    mocked_has_internet_connection.return_value = internet_connection_status
    mocked_valid_google_url.return_value = is_valid_url_status

    assert can_access_google_page('www.google.com') == awaited_result

