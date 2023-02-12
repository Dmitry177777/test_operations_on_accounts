import json
import random

from data.operations import Operations

def load_data():
  """ функция загрузки данных из файла """

  with open("E:/Python_SqyPro/3_basics_of_backend/12.3/Operations_on_accounts/data/operations.jonson", mode='r', encoding='utf-8') as file:
    data = json.load(file)
  return data


def init_operation(data):
  """aetrwbz инициализирtn класс Operation"""

  for i in range(len(data)):
    print(i)
    operations = Operations(data[i])
    print(f"{operations}")
  return operations

data=load_data()
init_operation(data)