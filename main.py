import json
from function import dict_sort, format_data

FILE = 'operate.json'

def main():
    """функция получает данные из файла operate.json и сортирует их с помощью dict_sort
    затем выводит последние 5 операций по дате"""
    with open('operate.json', 'r', encoding='utf-8') as file:
        dict = json.load(file)

    data = dict_sort(dict)

    for i in range(5):
        print(format_data(data[i]))






if __name__ == main():
    main()

