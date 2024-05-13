from src.utils import get_user_operation


def test_get_user_operation():
    assert get_user_operation(item={
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
    }) == "08.12.2019 Открытие вклада\nСчет **5907\n41096.24 USD"
