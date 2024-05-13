import json
from typing import Any


def get_list_operation():
    """
    Открывает и сортерует json файл
    """
    with open('operations.json', 'rt', encoding='utf-8') as file:
        list_operation = json.load(file)

    new_operation = []
    for operation in list_operation:
        if operation.get('state') == 'EXECUTED':
            new_operation.append(operation)

    sort_operation = sorted(new_operation, key=lambda x: x['date'], reverse=True)
    return sort_operation


def get_user_operation(item: dict[str, Any]):
    """
    Получает по ключу нужные значения,
    и возвращает в изменённом формате
    """
    date = get_date(item.get('date'))
    description = item.get('description')
    from_ = get_from(item.get('from'))
    to_ = get_to(item.get('to'))
    amount_ = item.get('operationAmount').get('amount')
    currency_ = item.get('operationAmount').get('currency').get('name')

    return f'{date} {description}\n{from_}{to_}\n{amount_} {currency_}'


def get_date(date):
    """
    Возвращает дату в читаемом формате
    """
    date_split = date[0:10].split(sep='-')
    return f'{date_split[2]}.{date_split[1]}.{date_split[0]}'


def get_from(from_):
    """
    Возвращает частично замаскированный номер счета отправителя
    """
    if from_ is None:
        return ''
    else:
        number = from_.split(' ')
        number_1 = number[-1]
        number_1.split(' ')
        if number[0] == 'Счет':
            return f'{number[0]} **{number_1[-4:]} -> '
        return f'{' '.join(number[:-1])} {number_1[:4]} {number_1[4:6]}** **** {number_1[-4:]} -> '


def get_to(to_):
    """
    Возвращает частично замаскированный номер счета получателя
    """
    number = to_.split(' ')
    number_1 = number[-1]
    number_1.split(' ')
    return f'{number[0]} **{number_1[-4:]}'
