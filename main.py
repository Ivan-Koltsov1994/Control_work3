from utils import get_date, data_sort, last_value, get_formatted_data

# Cсылка на данные по банковским переводам
URL = 'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1676472877077&signature=-pqIFmI-Dozg7b14YkgxK8haTqeT0d2-VrH3nPfBOTY&downloadName=operations.json'

# Приветствуем пользователя, просим ввести имя
User = input('Вас приветствует банк Vabank!\nВведите свое имя:\n')

# Количество последних банковских операций
LAST_VALUES = int(input(f'{User}, введите требуемое количество операций:\n'))

# Вводим отслеживание адреса отправителя
check_addres = input("Отслеживаем адрес отправителя: да/нет\n")
if check_addres.lower() == 'да':
    ADDRES_FROM = True
else:
    ADDRES_FROM = False


def main(url, last_values, address_from):
    """Функция получает ссылку на совершенные клиентом банка операции, количество выводимых операций,
    необходимость отслеживания обратного адреса отправителя и
    возвращает и выводит  последние  выполненные (EXECUTED) операций  на экран"""

    data, info = get_date(URL)  # Выводим статус получения данных
    if not data:
        exit(info)
    else:
        print(info)

    data = data_sort(data, ADDRES_FROM=address_from)  # Сортируем данные по дате
    data = last_value(data, last_values)  # Выбирает EXECUTED операции
    data = get_formatted_data(data)  # Вриводим к нужному формату

    # Выводим отсортированные данные на экран
    print(f"\nПоследние {last_values} выполненных операций: \n")
    for i in data:
        print(i, end='\n')


if __name__ == '__main__':
    main(URL, LAST_VALUES, ADDRES_FROM)