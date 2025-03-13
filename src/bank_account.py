from datetime import datetime
class BankAccount:
    def __init__(self, balance=0, log_file = None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("Cuenta creada")

    def _log_transaction(self,message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")



    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Retiro {amount}. Nuevo balance: {self.balance}.")
        return self.balance
    
    def withdraw(self,amount):
        weekend = [5,6]
        now = datetime.now()
        day = now.weekday()
        hr = now.hour
        if day in weekend:
            raise Exception("The Services only works on weekdays.")
        if hr < 8 or hr > 17:
            raise Exception("Services hours are from 8:00 a.m to 5:00 p.m.")
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdra succed. Balance: {self.balance}")
        return self.balance
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, acount):
        if amount > self.balance:
            self._log_transaction(f"Intento de transferencia. Saldo insuficiente!")
            raise ValueError('Saldo insuficiente!')
        self.balance -= amount
        acount.balance += amount
        self._log_transaction(f"Transferencia exitosa. Valor transferido: {amount}.\nBalance: {self.balance}")
        return self.get_balance(),acount.get_balance