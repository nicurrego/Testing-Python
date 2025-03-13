from datetime import datetime

now = datetime.now().weekday()
print(now)

def withdraw(amount):
        weekend = [5,6]
        now = datetime.now()
        # day = now.weekday()
        day = 5
        hr = now.hour
        print(day)
        if day in weekend:
            raise Exception("The Services only works on weekdays.")
        if hr < 8 or hr > 17:
            raise Exception("Services hours are from 8:00 a.m to 5:00 p.m.")
        if amount > 0:
             print('hola')
        #     self.balance -= amount
        #     self._log_transaction(f"Withdra succed. Balance: {self.balance}")
        # return self.balance

withdraw(15)