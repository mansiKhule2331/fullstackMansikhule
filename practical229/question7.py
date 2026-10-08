class ATM:

  def __init__(self, pin, balance=0.0):
    self.pin = pin
    self.balance = balance
    self.is_authenticated = False

  def verify_pin(self, entered_pin):
    """Verifies if the entered PIN matches the account PIN."""
    if entered_pin == self.pin:
      self.is_authenticated = True
      print("PIN verification successful.")
      return True
    else:
      print("Invalid PIN.")
      return False

  def check_balance(self):
    """Returns the current account balance if authenticated."""
    if not self.is_authenticated:
      print("Please verify your PIN first.")
      return None
    print(f"Current Balance: ₹{self.balance:.2f}")
    return self.balance

  def deposit(self, amount):
    """Deposits a specified amount into the account."""
    if not self.is_authenticated:
      print("Please verify your PIN first.")
      return
    if amount > 0:
      self.balance += amount
      print(f"Successfully deposited ₹{amount:.2f}")
      self.check_balance()
    else:
      print("Deposit amount must be greater than zero.")

  def withdraw(self, amount):
    """Withdraws a specified amount if funds are sufficient."""
    if not self.is_authenticated:
      print("Please verify your PIN first.")
      return
    if amount <= 0:
      print("Withdrawal amount must be greater than zero.")
    elif amount > self.balance:
      print("Insufficient funds for this withdrawal.")
    else:
      self.balance -= amount
      print(f"Successfully withdrew ₹{amount:.2f}")
      self.check_balance()


# --- Example Usage ---
if __name__ == "__main__":
  # Initialize ATM with PIN '1234' and starting balance of ₹5000.00
  my_atm = ATM(pin="1234", balance=5000.00)

  # Try actions before verifying PIN
  my_atm.check_balance()

  # Verify PIN
  my_atm.verify_pin("1234")

  # Check balance
  my_atm.check_balance()

  # Deposit money
  my_atm.deposit(1500.00)

  # Withdraw money
  my_atm.withdraw(2000.00)

  # Try withdrawing more than available
  my_atm.withdraw(10000.00)