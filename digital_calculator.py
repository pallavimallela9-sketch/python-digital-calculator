print("==========================================")
print("            DIGITAL CALCULATOR")
print("==========================================")

history = []

while True:
    print("\n============== MENU ==============")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. View Calculation History")
    print("8. Clear History")
    print("9. Exit")
    print("==================================")

    choice = input("Enter your choice: ")

    if choice == "9":
        print("\nThank you for using the Digital Calculator.")
        break

    elif choice == "7":
        if not history:
            print("No calculations available.")
        else:
            print("\n========== CALCULATION HISTORY ==========")

            for index, calculation in enumerate(history, start=1):
                print(index, ".", calculation)

    elif choice == "8":
        history.clear()
        print("Calculation history cleared.")

    elif choice in ["1", "2", "3", "4", "5", "6"]:
        try:
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))

            if choice == "1":
                result = first + second
                operator = "+"

            elif choice == "2":
                result = first - second
                operator = "-"

            elif choice == "3":
                result = first * second
                operator = "*"

            elif choice == "4":
                if second == 0:
                    print("Division by zero is not allowed.")
                    continue

                result = first / second
                operator = "/"

            elif choice == "5":
                if second == 0:
                    print("Modulus by zero is not allowed.")
                    continue

                result = first % second
                operator = "%"

            elif choice == "6":
                result = first ** second
                operator = "**"

            calculation = f"{first} {operator} {second} = {result}"
            history.append(calculation)

            print("\nResult:", result)

        except ValueError:
            print("Please enter valid numbers.")

    else:
        print("Invalid choice. Please try again.")
