class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def display_balance(self):
        print(f"Current balance for {self.account_holder}: ${self.balance:.2f}")


# Example usage:
account = BankAccount("Anil", 1000.0)
account.display_balance()  # Current balance: $1000.00
account.deposit(500.0)  # Deposited $500.00. New balance: $1500.00
account.withdraw(200.0)  # Withdrew $200.00. New balance: $1300.00
account.withdraw(2000.0)  # Insufficient funds for this withdrawal.