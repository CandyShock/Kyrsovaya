from function import format_data, blurring_card, refactor_date, dict_sort
import pytest

def test_ref_data():
    assert refactor_date("2018-06-08T16:14:59.936274") == '08.06.2018'
    assert refactor_date("2011-05-07T16:14:59.936274") == '07.05.2011'

@pytest.mark.parametrize('str_card, mask', [("Maestro 7552745726849311", "Maestro 7552 74** **** 9311"),
                                            ("Счет 82781399328834147668", "Счет **7668"),
                                            ("Visa Gold 2684274847577419", "Visa Gold 2684 27** **** 7419")])

def test_blur_card(str_card, mask):
    assert blurring_card(str_card) == mask


def test_format():
    data ={
    "id": 317987878,
    "state": "EXECUTED",
    "date": "2018-01-13T13:00:58.458625",
    "operationAmount": {
      "amount": "55985.82",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Classic 8906171742833215",
    "to": "Visa Platinum 6086997013848217"
  }
    result = "13.01.2018 Перевод с карты на карту\nVisa Classic 8906 17** **** 3215 -> Visa Platinum 6086 99** **** 8217\n55985.82 USD"

    assert format_data(data) == result

def test_dict_sort():
    data = [
    {
    "id": 172864002,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364"
    },
    {
    "id": 536723678,
    "state": "EXECUTED",
    "date": "2018-07-03T18:35:29.512364"
    },
    {
    "id": 41428829,
    "state": "Open",
    "date": "2017-07-03T18:35:29.512364"
    }
    ]

    result = [
    {
    "id": 172864002,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364"
    },
    {
    "id": 536723678,
    "state": "EXECUTED",
    "date": "2018-07-03T18:35:29.512364"
    }
    ]

    assert dict_sort(data) == result
