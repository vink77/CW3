import pytest
@pytest.fixture
def test_data():
    return [
      {
        "id": 716496732,
        "state": "EXECUTED",
        "date": "2018-04-04T17:33:34.701093",
        "operationAmount": {
          "amount": "40701.91",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод организации",
        "from": "Visa Gold 5999414228426353",
        "to": "Счет 72731966109147704472"
      },
      {
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
      },
      {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
          "amount": "67314.70",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
      },
      {
        "id": 615064591,
        "state": "CANCELED",
        "date": "2018-10-14T08:21:33.419441",
        "operationAmount": {
          "amount": "77751.04",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 3928549031574026",
        "to": "Счет 84163357546688983493"
      },
      {
        "id": 147815167,
        "state": "EXECUTED",
        "date": "2018-01-26T15:40:13.413061",
        "operationAmount": {
          "amount": "50870.71",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 4598300720424501",
        "to": "Счет 43597928997568165086"
      }
    ]
