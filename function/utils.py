import json
from data.operations import Bank_operations

def load_data():
  """ функция загрузки данных из файла """

  with open("E:/Python_SqyPro/3_basics_of_backend/12.3/Operations_on_accounts/data/operations.jonson", mode='r', encoding='utf-8') as file:
    data = json.load(file)

  #сортировка по дате ( в начале последние даты )
  data.sort(key=lambda x: x.get('date',""), reverse=True)

  return data

def init_operation(data):
  """функция инициализации класса Operation (5 последних позиций)"""

  for i in range(5):
    #print(i)
    operations = Bank_operations(data[i])
    operations.check_list()

# Загружаем базу с сортированными данными операции
data=load_data()

# Инициализируем класс Bank_operations, 5 последних операций
operations = init_operation(data)


