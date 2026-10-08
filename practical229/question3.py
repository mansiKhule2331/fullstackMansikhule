def calculate_bonus(salary, years_of_experience):
    """
    Calculates employee bonus based on salary and years of experience.
    
    Rules:
    - More than 10 years: 20% bonus
    - 5 to 10 years: 15% bonus
    - 2 to 4 years: 10% bonus
    - Less than 2 years: 5% bonus
    """
    if years_of_experience > 10:
        bonus_percentage = 0.20
    elif years_of_experience >= 5:
        bonus_percentage = 0.15
    elif years_of_experience >= 2:
        bonus_percentage = 0.10
    else:
        bonus_percentage = 0.05
        
    bonus_amount = salary * bonus_percentage
    total_salary = salary + bonus_amount
    
    return bonus_percentage * 100, bonus_amount, total_salary

def main():
    print("--- Employee Bonus Calculator ---")
    try:
        # Taking inputs from the user
        salary = float(input("Enter employee's basic salary: "))
        years_of_experience = float(input("Enter years of experience: "))
        
        if salary < 0 or years_of_experience < 0:
            print("Error: Salary and years of experience must be positive numbers.")
            return

        # Performing calculation
        percentage, bonus, total = calculate_bonus(salary, years_of_experience)
        
        # Displaying results
        print("\n--- Calculation Results ---")
        print(f"Bonus Percentage applied : {percentage}%")
        print(f"Calculated Bonus Amount  : ${bonus:,.2f}")
        print(f"Total Payout (With Bonus): ${total:,.2f}")
        
    except ValueError:
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    main()