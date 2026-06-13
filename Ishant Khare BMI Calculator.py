def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:
        return "Normal weight"
    elif 25.0 <= bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

def run_bmi_calculator():
    print("=========================================")
    print("            BMI CALCULATOR               ")
    print("=========================================")
    
    try:
        weight_input = input("Enter your weight in kilograms (e.g. 70): ").strip()
        weight = float(weight_input)
        if weight <= 0:
            print("Error: Weight must be a positive number greater than zero.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a valid number for weight.")
        return

    try:
        height_input = input("Enter your height in meters (e.g. 1.75): ").strip()
        height = float(height_input)
        if height <= 0:
            print("Error: Height must be a positive number greater than zero.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a valid number for height.")
        return

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print("\n-----------------------------------------")
    print(f"Your Weight:   {weight} kg")
    print(f"Your Height:   {height} m")
    print(f"Calculated BMI: {bmi:.2f}")
    print(f"Classification: {category}")
    print("-----------------------------------------")

    print("\nStandard BMI Categories:")
    print("  * Underweight: < 18.5")
    print("  * Normal weight: 18.5 - 24.9")
    print("  * Overweight: 25 - 29.9")
    print("  * Obese: >= 30")
    print("=========================================")

if __name__ == "__main__":
    while True:
        run_bmi_calculator()
        print()
        again = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if again != "yes" and again != "y":
            print("\nThank you for using the BMI Calculator. Stay healthy!")
            break
        print()
