import unittest
from data import operations

class TestOperations(unittest.TestCase):
    def setUp(self):
      test_data = {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890',
                   'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
                   'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012',
                   'to': 'Счет 35158586384610753655'}

      self.test_object = operations.Bank_operations(test_data)
    def test_check(self):
      self.assertEqual(self.test_object.check_list(), ('07.12.2019 Перевод организации\n'
                                                       'Visa Classic xxxxxxxx93689012 -> Счет xxxxxxxx384610753655\n'
                                                       '48150.39 USD\n'
                                                       '\n'
                                                       ' '))

    def test_list(self):
      self.assertEqual(self.test_object.x_list('Счет 90424923579946435907', 8),
                       'Счет xxxxxxxx579946435907')
      self.assertEqual(self.test_object.x_list('Visa Classic 1203468193689012', 8),
                       'Visa Classic xxxxxxxx93689012')


if __name__ == '__main__':
    unittest.main()