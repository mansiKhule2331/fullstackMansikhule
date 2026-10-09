# Create a Car class
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # Method to display car details
    def display(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Price :", self.price)


# Create two objects
car1 = Car("Tata", "Nexon", 900000)
car2 = Car("Hyundai", "Creta", 1200000)

# Display details
print("--- Car 1 Details ---")
car1.display()

print("\n--- Car 2 Details ---")
car2.display()