from mock.myapp.dice import roll_dice
import requests

def guess_number(num):
    result = roll_dice()
    if result == num:
        return "Congratulations, you guessed correctly!"
    else:
        return f"Sorry, the correct number was {result}."

''' from unittest import mock
def roll dice....
 mock_roll_dice = mock.Mock(name ="roll dice mock", return_value = 3 )  VIA  TELLING THE PRED VALUE
mock_roll_dice.assert_called()  TELLIN  HOW MANY TIMES IT CALLED

 
 mock_roll_dice()   GIVING US A ADDRESS
 '''

def get_ip():
    response= requests.get("https://httpbin.org/ip")   # https://httpbin.org/ip
    if response.status_code == 200:
        return response.json()["origin"]
