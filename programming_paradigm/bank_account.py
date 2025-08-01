class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.1f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            return True
        else:
            print(
                "Withdrawal amount must be positive and less than or equal to the balance."
            )
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.1f}")


# Optional: Only runs when executing this file directly
if __name__ == "__main__":
    account = BankAccount(10000)
    account.deposit(50000)
    account.withdraw(30000)
    account.display_balance()
