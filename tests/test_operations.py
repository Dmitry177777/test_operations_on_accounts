import unittest
from data import operations

class TestOperations(unittest.TestCase):

  def setUp(self):
    self.date= '26.08.2019'
    self.description='Перевод организации'
    self.from_ = 'Maestro 1596837868705199'
    self.to = 'Счет 64686473678894779589'
    self.from_check=''
    self.to_check=''
    self.amount= '31957.58'
    self.currency_name = 'руб.'

  def test_check(self):
    self.from_check = 'Maestro xxxxxxxx68705199'
    self.to_check = 'Счет xxxxxxxx678894779589'
    self.assertEqual(f'{self.date} {self.description}\n{self.from_check} -> {self.to_check}\n{self.amount} {self.currency_name}\n\n ',f'26.08.2019 Перевод организации\nMaestro xxxxxxxx68705199 -> Счет xxxxxxxx678894779589\n31957.58 руб.\n\n ')



  def test_list(self):
    self.assertEqual(operations.Bank_operations.x_list(self, self.from_ , 8), 'Maestro xxxxxxxx68705199')
    self.assertEqual(operations.Bank_operations.x_list(self, self.to, 8), 'Счет xxxxxxxx678894779589')


if __name__ == '__main__':
    unittest.main()

