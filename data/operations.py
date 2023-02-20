
class Bank_operations ():
    """"Класс банковские операции"""
    def __init__(self, i):
        self.id = i.get ('id')  #номер "id":
        self.state = i.get('state') #"state":
        self.date_full = i.get('date') # формат 2019-12-08T22:46:21.935582
        self.date = f"{self.date_full[8:10]}.{self.date_full[5:7]}.{self.date_full[:4]}"  # формат 08.12.2019  #прошлый формат  2019-12-08T22:46:21.935582
        self.amount = i.get ('operationAmount',{}).get('amount')  # "operationAmount":"amount":
        self.currency_name = i.get ('operationAmount',{}).get('currency',{}).get('name')  # "operationAmount":"currency": "name":
        self.currency_code = i.get('operationAmount',{}).get('currency',{}).get('code') # "operationAmount":"currency": "code":
        self.description = i.get('description')  # "description":
        self.from_ = i.get ('from', "") # "from":
        self.to = i.get ('to') # "to":
        self.from_check =''
        self.to_check=''



    def __repr__(self):
        return f'{self.date} {self.description}\n\n '


    def check_list (self):
        """Метод выводящий скрытые персональные банковские данные"""


        self.from_check = self.x_list(self.from_, 8)
        self.to_check = self.x_list(self.to, 8)

        method_output = (f'{self.date} {self.description}\n{self.from_check} -> {self.to_check}\n{self.amount} {self.currency_name}\n\n ')

        return method_output


    def x_list (self, check, k):
      """Метод скрывающий данные банковской карты и счета"""

      list_x = list(check)

      if len(list_x) > 0:
        x = len(list_x) - list_x[::-1].index(" ")   # поиск индекса пробела с конца строки
      return "".join([list_x[i] if i < x or i >= x + k else "x" for i in range(len(list_x))])


