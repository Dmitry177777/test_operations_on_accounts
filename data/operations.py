
class Operations ():

    def __init__(self, i):
        self.id = i.get ('id')  #номер "id":
        self.state = i.get('state') #"state":
        self.date = i.get('date')  # "date"
        self.amount = i.get ('operationAmount',{}).get('amount')  # "operationAmount":"amount":
        self.currency_name = i.get ('operationAmount',{}).get('currency',{}).get('name')  # "operationAmount":"currency": "name":
        self.currency_code = i.get('operationAmount',{}).get('currency',{}).get('code') # "operationAmount":"currency": "code":
        self.description = i.get('description')  # "description":
        self.from_ = i.get ('from') # "from":
        self.to = i.get ('to') # "to":

    def __repr__(self):
        return f'Операция номер: {self.id} - карта: {self.description}'


    def sorted_ (self):
        """сортировка date """
        sorted(operations, key=lambda оperations: operations.date)


    def is_check_five_operations (self):
        """ выборка 5 последних операций """
        pass