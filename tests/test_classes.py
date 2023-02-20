from utils.classes import ClientOperations
from utils.utils import load_data

def test_get_need_transactions():
    test_case_1 = load_data("operations.json")
    expected = [{
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
  }]
    test_object = ClientOperations(test_case_1)
    assert(test_object.get_need_transactions("EXECUTED", 1)) == expected