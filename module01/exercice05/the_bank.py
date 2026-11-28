class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name

        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
        
    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts: list[Account] = []

    def add(self, new_account: Account):
        if not new_account or not isinstance(new_account, Account):
            return False 
        elif new_account in self.accounts:
            return False
        self.accounts.append(new_account)
        return True

    def transfert(self, origin: Account, dest: Account, amount: float):
        if amount < 0 or amount > origin.value:
            return False
        self.check_validity(origin)
        return True

    def fix_account(self, name):
        if not name or not isinstance(name , str):
            return False
        return True

    def check_validity(self, account: Account):
        for atrr in dir(account):
            if not atrr.startswith("__"):
                print(atrr)
                print(account.__getattribute__(atrr))

account1= Account("1", value = 200)
account2 = Account("2", value = 200)

bank = Bank()

bank.add(account1)
bank.add(account2)

bank.transfert(origin=account1, dest=account2, amount=100)