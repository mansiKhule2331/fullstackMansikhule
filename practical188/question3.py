import math

def calculate_circle_area():
    print("\n--- Circle Area Calculator ---")
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is: {area:.2f}")

def calculate_rectangle_area():
    print("\n--- Rectangle Area Calculator ---")
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area:.2f}")

def calculate_triangle_area():
    print("\n--- Triangle Area Calculator ---")
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area:.2f}")

def main():
    while True:
        print("\n================================")
        print("         AREA CALCULATOR        ")
        print("================================")
        print("1. Calculate Area of a Circle")
        print("2. Calculate Area of a Rectangle")
        print("3. Calculate Area of a Triangle")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            calculate_circle_area()
        elif choice == '2':
            calculate_rectangle_area()
        elif choice == '3':
            calculate_triangle_area()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option (1-4).")

if __name__ == "__main__":
    main()