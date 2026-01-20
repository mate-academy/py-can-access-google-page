from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet,valid_url,result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Available internet and valid url"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Available internet and invalid url"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Unavailable internet and valid url"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="Unavailable internet and invalid url"
        )
    ]
)
def test_output_with_different_values_of_url_internet(
        internet: bool,
        valid_url: bool,
        result: str
) -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_internet:
        mocked_internet.return_value = internet
        with mock.patch("app.main.valid_google_url") as mocked_url_validator:
            mocked_url_validator.return_value = valid_url
            assert (
                can_access_google_page("") == result
            ), (f"Function should return {result} when "
                f"`has_internet_connection()` is {internet} and "
                f"`valid_google_url()` is {valid_url}")


@pytest.mark.parametrize(
    "function",
    [
        pytest.param(
            "app.main.valid_google_url",
            id="`valid_google_url()` should be called"
        ),
        pytest.param(
            "app.main.has_internet_connection",
            id="`has_internet_connection()` should be called"
        )
    ]
)
def test_functions_should_be_called(function: str) -> None:
    with mock.patch(function) as mocked_function:
        can_access_google_page("https://google.com")
        mocked_function.assert_called_once()
