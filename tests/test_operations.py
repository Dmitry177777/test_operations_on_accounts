import unittest
from data.operations import Bank_operations


class TestOperations(unittest.TestCase):

  def setUp(self, i):
    self.operations = Bank_operations(i)
    print(self.operations)

  # def test_check(self):
  #   self.assertEqual(self.operations.check_list(), print( f'{self.date} {self.description}\n{self.from_check} -> {self.to_check}\n{self.amount} {self.currency_name}\n\n '))

  def test_list(self):
    check = 'Счет 90424923579946435907'
    k = 8
    print(self.operations.x_list(check, k))
    self.assertEqual(self.operations.x_list(check, k), 'Счет xxxxxxxx579946435907')

if __name__ == '__main__':
    unittest.main()

    # self.id = i.get('id')  # номер "id":
    # self.state = i.get('state')  # "state":
    # self.date_full = i.get('date')  # формат 2019-12-08T22:46:21.935582
    # self.date = f"{self.date_full[8:10]}.{self.date_full[5:7]}.{self.date_full[:4]}"  # формат 08.12.2019  #прошлый формат  2019-12-08T22:46:21.935582
    # self.amount = i.get('operationAmount', {}).get('amount')  # "operationAmount":"amount":
    # self.currency_name = i.get('operationAmount', {}).get('currency', {}).get(
    #     'name')  # "operationAmount":"currency": "name":
    # self.currency_code = i.get('operationAmount', {}).get('currency', {}).get(
    #     'code')  # "operationAmount":"currency": "code":
    # self.description = i.get('description')  # "description":
    # self.from_ = i.get('from', "")  # "from":
    # self.to = i.get('to')  # "to":
    # self.from_check = ''
    # self.to_check = ''