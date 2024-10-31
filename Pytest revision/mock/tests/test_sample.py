from mock.myapp.sample import guess_number,  get_ip
from unittest import mock
import pytest

@pytest.mark.parametrize("_input, expected", [(3, "Congratulations, you guessed correctly!"), (4, "Sorry, the correct number was 4.")])
@mock.patch("mock.myapp.sample.roll_dice")
def test_guess_number(mock_roll_dice,_input,expected):
    mock_roll_dice.return_value =   4
    assert guess_number(_input) == expected
    mock_roll_dice.assert_called_once()


@mock.patch("mock.myapp.sample.requests.get")
def test_get_ip(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(name="mock response",
                                               **{"status_code": 200, "json.return_value": {"origin": "0.0.0.0"}})

    assert get_ip() == "0.0.0.0"
    mock_requests_get.assert_called_once_with("https://httpbin.org/ip")