class BankAccount:
    total_accounts = 0

    def __init__(self, account_type):
        self.__balance = 0
        self._account_number = f"ACC{BankAccount.total_accounts + 1}"
        self.account_type = account_type
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)

    def withdraw(self, amount):
        if self.__can_withdraw(amount):
            self.__update_balance(-amount)

    def get_balance(self):
        return self.__balance

    def __update_balance(self, amount):
        self.__balance += amount

    def __can_withdraw(self, amount):
        return amount <= self.__balance

    def __str__(self):
        return f"Счет {self._account_number} ({self.account_type}) — Баланс: {self.__balance} единиц."


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_type):
        account = BankAccount(account_type)
        self.accounts.append(account)
        return account

    def get_total_accounts(self):
        return BankAccount.total_accounts

bank = Bank()

# Создание счетов
account1 = bank.create_account("Текущий")
account2 = bank.create_account("Сберегательный")

# Пополнение счетов
account1.deposit(1000)
account2.deposit(500)

# Снятие средств
account1.withdraw(200)

# Получение информации о счетах
print(account1)  # Счет ACC1 (Текущий) — Баланс: 800 единиц.
print(account2)  # Счет ACC2 (Сберегательный) — Баланс: 500 единиц.

# Общее количество счетов
print("Всего счетов:", bank.get_total_accounts())  # Всего счетов: 2
