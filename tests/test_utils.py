rom utils import get_date, data_sort, last_value, get_formatted_data
import pytest

def test_get_data(test_url):
    """Тестируем функцию get_date"""

    assert (len(get_date(test_url)[0])) > 0
    assert get_date("https://file.notion.so/")[0] is None
    assert get_date("https://github.com/Ivan-Koltsov1994/git_project_new/blob/main/str_func.py")[0] is None
    assert get_date("https://github.com/git_project_new/blob/main/str_func.py")[0] is None
    assert get_date("https://github.com/arhipov-proA/lesson_11_2")[0] is None
    assert get_date("https://github.com/arhipov-proA/lesson_11_3")[0] is None


def test_data_sort(test_data, ADDRES_FROM=False):
    """Тестируем функцию data_sort. Тесты подобраны LAST_VALUES = 5"""

    assert len(data_sort(test_data, ADDRES_FROM=False)) == 4
    assert len(data_sort(test_data, ADDRES_FROM=True)) == 2


def test_last_valuse(test_data):
    """Тестируем функцию last_valuse. Тесты подобраны LAST_VALUES = 5"""

    data = last_value(test_data, 5)
    assert data[0]["date"] == '2019-07-03T18:35:29.512364'
    assert len(data) == 5


def test_get_formatted_data(test_data):
    """Тестируем функцию formatted_data. Тесты подобраны LAST_VALUES = 5"""

    data = get_formatted_data(test_data)
    print(data)
    assert data == [
        '***********************************************************************************\n03.07.2019  Перевод организации\n\nMasterCard  7158 30** ****6758 -> Счет **5560\n\n8221.37 USD\n***********************************************************************************\n',
        '***********************************************************************************\n04.04.2019  Перевод со счета на счет\n\n   -> Счет **4188\n\n79114.93 USD\n***********************************************************************************\n',
        '***********************************************************************************\n30.06.2018  Перевод организации\n\nСчет  7510 68** ****6952 -> Счет **6702\n\n9824.07 USD\n***********************************************************************************\n',
        '***********************************************************************************\n23.03.2018  Открытие вклада\n\n   -> Счет **2431\n\n48223.05 руб.\n***********************************************************************************\n',
        '***********************************************************************************\n26.08.2009  Перевод организации\n\nMaestro  1596 83** ****5199 -> Счет **9589\n\n31957.58 руб.\n***********************************************************************************\n']
