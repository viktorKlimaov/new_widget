import json


def get_list_operation():
    with open('operations.json', 'rt', encoding='utf-8') as file:
        list_operation = json.load(file)

    new_operation = []
    for operation in list_operation:
        if operation.get('state') == 'EXECUTED':
            new_operation.append(operation)

    sort_operation = sorted(new_operation, key=lambda x: x['date'], reverse=True)
    return sort_operation
