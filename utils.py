import requests
from datetime import datetime


def get_date(URL):
    """Функция получает ссылку на совершенные клиентом банка операции, возвращает данные в json формате,
    выводит статус получения данных"""

    try:
        response = requests.get(URL)
        if response.status_code == 200:
            return response.json(), 'INFO:Данные получены успешно'
        return None, f'ERROR:status_code:{response.status_code} \n'
    except requests.exceptions.JSONDecodeError:
        return None, 'ERROR:requests.exceptions.JSONDecodeError \n'
    except requests.exceptions.ConnectionError:
        return None, 'ERROR:requests.exceptions.ConnectionError \n'


def data_sort(data, ADDRES_FROM=False):
    """Функция выбирает успешные (EXECUTED) банковские операции, учитывает есть ли данные отправителя"""

    data = [x for x in data if x.get("state") == "EXECUTED"]
    if ADDRES_FROM:
        data = [x for x in data if "from" in x]
    return data


def last_value(data, count_last_values):
    """Функция сортирует операции по дате, возвращает LAST_VALUES последних операций"""

    data = sorted(data, key=lambda x: x["date"], reverse=True)
    data = data[:count_last_values]
    return data


def get_formatted_data(data):
    """Функция форматирует и возвращет операции в виде
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб."""

    formatted_data = []
    for row in data:

        date = datetime.strptime(row.get("date"), "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")

        description = row.get("description")

        sunder_id, sunder_card = '', ''

        if "from" in row:
            sender = row['from'].split()
            sunder_id = sender[-1]
            sunder_id = f'{sunder_id[:4]} {sunder_id[4:6]}** ****{sunder_id[-4:]}'
            sunder_card = ' '.join(sender[0:-1])

        recipient = row['to'].split()
        recipient_id = recipient[-1]
        recipient_id = f'**{recipient_id[-4:]}'
        recipient_card = recipient[0]

        operation_money = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"

        formatted_data.append(f"""***********************************************************************************
{date}  {description}\n
{sunder_card}  {sunder_id} -> {recipient_card} {recipient_id}\n
{operation_money}
***********************************************************************************
""")

    return formatted_data
