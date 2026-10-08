def main():
    # Initialize an empty list
    my_list = []

    while True:
        # Display the menu options
        print("\n=== Python List Operations Menu ===")
        print("1. Insert an element")
        print("2. Delete an element")
        print("3. Search an element")
        print("4. Display all elements")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            element = input("Enter the element to insert: ")
            position_type = input("Insert at the end? (yes/no): ").strip().lower()
            
            if position_type == 'no':
                try:
                    index = int(input(f"Enter the index position (0 to {len(my_list)}): "))
                    my_list.insert(index, element)
                    print(f"Success: '{element}' inserted at index {index}.")
                except ValueError:
                    print("Error: Invalid index. Please enter an integer.")
            else:
                my_list.append(element)
                print(f"Success: '{element}' appended to the end of the list.")

        elif choice == '2':
            if not my_list:
                print("The list is empty. Nothing to delete.")
                continue
                
            element = input("Enter the exact element value to delete: ")
            if element in my_list:
                my_list.remove(element)
                print(f"Success: The first occurrence of '{element}' has been deleted.")
            else:
                print(f"Error: Element '{element}' not found in the list.")

        elif choice == '3':
            if not my_list:
                print("The list is empty. Nothing to search.")
                continue

            element = input("Enter the element to search for: ")
            if element in my_list:
                # Find all occurrences of the index
                indices = [str(i) for i, x in enumerate(my_list) if x == element]
                print(f"Found! '{element}' is present at index/indices: {', '.join(indices)}")
            else:
                print(f"'{element}' was not found in the list.")

        elif choice == '4':
            if not my_list:
                print("The list is currently empty [ ].")
            else:
                print("\nCurrent List Elements:")
                for index, item in enumerate(my_list):
                    print(f"Index {index}: {item}")
                print(f"Raw format: {my_list}")

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option from 1 to 5.")

if __name__ == "__main__":
    main()