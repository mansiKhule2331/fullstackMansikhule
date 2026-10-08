def generate_bill():
    products = []
    grand_total = 0

    print("--- Welcome to the Billing System ---")
    print("Enter product details below. Type 'done' as the product name to finish.\n")

    # Step 1: Loop to collect product details from the user
    while True:
        name = input("Enter product name (or 'done' to calculate bill): ").strip()
        
        # Break the loop if user is finished adding products
        if name.lower() == 'done':
            break
            
        if not name:
            print("Product name cannot be empty. Please try again.")
            continue

        # Get valid price input
        try:
            price = float(input(f"Enter price for '{name}': "))
            if price <= 0:
                print("Price must be greater than 0. Please try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a numerical value for price.")
            continue

        # Get valid quantity input
        try:
            quantity = int(input(f"Enter quantity for '{name}': "))
            if quantity <= 0:
                print("Quantity must be greater than 0. Please try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a whole number for quantity.")
            continue

        # Calculate individual item total
        item_total = price * quantity
        grand_total += item_total

        # Store product details in a list of dictionaries
        products.append({
            'name': name,
            'price': price,
            'quantity': quantity,
            'total': item_total
        })
        print(f"-> Added {quantity} x {name} successfully!\n")

    # Step 2: Generate and display the final bill receipt
    if not products:
        print("\nNo products were added. Thank you!")
        return

    print("\n" + "="*45)
    print(f"{'FINAL BILL RECEIPT':^45}")
    print("="*45)
    print(f"{'Product':<15} {'Price':<10} {'Qty':<6} {'Total':<10}")
    print("-"*45)

    for item in products:
        print(f"{item['name'].capitalize():<15} {item['price']:<10.2f} {item['quantity']:<6} {item['total']:<10.2f}")

    print("-"*45)
    print(f"{'GRAND TOTAL:':<33} ${grand_total:.2f}")
    print("="*45)
    print(f"{'Thank you for shopping with us!':^45}")

# Run the program
if __name__ == "__main__":
    generate_bill()