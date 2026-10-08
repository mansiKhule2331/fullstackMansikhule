class ElectricityBillCalculator:

  def __init__(self, units):
    self.units = units

  def calculate_bill(self):
    if self.units < 0:
      raise ValueError("Please enter a valid units consumed")

    bill = 0.0
    remaining_units = self.units

    # Slab 1: First 50 units at 0/unit
    if remaining_units <= 50:
      return 0.0

    rem_units = self.units - 50

    # Slab 2: 51 to 100 units at ₹5 per unit
    if rem_units <= 50:
      bill += rem_units * 5.0
      return round(bill, 2)
    else:
      bill += 50 * 5.0
      rem_units -= 50

    # Slab 3: 101 to 150 units at ₹10 per unit
    if rem_units <= 50:
      bill += rem_units * 10.0
      return round(bill, 2)
    else:
      bill += 50 * 10.0
      rem_units -= 50

    # Slab 4: 151 to 200 units at ₹15 per unit
    if rem_units <= 50:
      bill += rem_units * 15.0
      return round(bill, 2)
    else:
      bill += 50 * 15.0
      rem_units -= 50

    # Slab 5: Above 200 units at ₹20 per unit
    bill += rem_units * 20.0
    return round(bill, 2)


# Example Usage:
calc = ElectricityBillCalculator(220)
print(f"Total Bill: ₹{calc.calculate_bill()}")