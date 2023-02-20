import json
from data.operations import Bank_operations

def load_data(file_path_json ):
  """ функция загрузки данных из файла """

  with open(file_path_json , mode='r', encoding='utf-8') as file:
    data = json.load(file)

  #сортировка по дате ( в начале последние даты )
  data.sort(key=lambda x: x.get('date',""), reverse=True)
  return data

def init_operation(data):
  """функция инициализации класса Operation (5 последних позиций)"""

  operation_list = []

  for i in range(5):

    operations = Bank_operations(data[i])
    operation_list.append(operations.check_list())

  return operation_list



# устанавливаем путь к файлу с данными в формате json
file_path_json = "../data/operations.json"


# Загружаем базу с сортированными данными операции
data=load_data(file_path_json )


# Инициализируем класс Bank_operations, 5 последних операций
operations = init_operation(data)

# Вывод на печать 5-ти последних транзакций
print("".join([str(operations[i]) for i in range(len(operations))]))