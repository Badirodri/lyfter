# 1. Cree una clase de `BankAccount` que:
#     1. Tenga un atributo de `balance`.
#     2. Tenga un método para ingresar dinero.
#     3. Tengo un método para retirar dinero.

#     Cree otra clase que herede de esta llamada `SavingsAccount` que:

#     1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
#     2. Arroje un error si se intenta retirar dinero y el `balance` está debajo del `min_balance`.

class BankAccount():
  def __init__(self,balance):
    self.balance=balance

  def substract_money(self,amount):
    self.balance -= amount
    print(self.balance)

  def add_money(self, amount):
    self.balance += amount
    print(self.balance)

class SavingsAccount(BankAccount):

  def __init__(self, min_balance, balance):
    self.min_balance=min_balance
    super().__init__(balance)

  def create_transaction(self, amount):
    try:
      if self.balance - amount < self.min_balance:
        raise ValueError()
      else:
        self.substract_money(amount)
    except ValueError as err:
      print("Error: You dont have enough money")


transaction = SavingsAccount(0,250)
transaction.create_transaction(50)


transaction_2= SavingsAccount(0,0)
transaction_2.add_money(100)
transaction_2.create_transaction(200)
