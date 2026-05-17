# ================================
#     AMEER'S CALCULATOR 
#     Day 6 — #150DaysOfAI
# ================================

def calculator():
    print("=" * 40)
    print("     AMEER'S CALCULATOR ")
    print("     Day 6 — #150DaysOfAI")
    print("=" * 40)

    # User input
    num1 = float(input("\nEnter first number  : "))
    num2 = float(input("Enter second number : "))

    print("\nSelect Operation:")
    print("[1] Addition       (+)")
    print("[2] Subtraction    (-)")
    print("[3] Multiplication (*)")
    print("[4] Division       (/)")
    print("[5] Floor Division (//)")
    print("[6] Modulus        (%)")
    print("[7] Power          (**)")
    print("=" * 40)

    choice = input("Enter choice (1-7): ")

    print("=" * 40)

    if choice == "1":
        result = num1 + num2
        print(f"{num1} + {num2} = {result:.2f}")
    elif choice == "2":
        result = num1 - num2
        print(f"{num1} - {num2} = {result:.2f}")
    elif choice == "3":
        result = num1 * num2
        print(f"{num1} × {num2} = {result:.2f}")
    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by 0! ")
        else:
            result = num1 / num2
            print(f"{num1} ÷ {num2} = {result:.2f}")
    elif choice == "5":
        if num2 == 0:
            print("Error: Cannot divide by 0! ")
        else:
            result = num1 // num2
            print(f"{num1} // {num2} = {result:.0f}")
    elif choice == "6":
        result = num1 % num2
        print(f"{num1} % {num2} = {result:.2f}")
    elif choice == "7":
        result = num1 ** num2
        print(f"{num1} ^ {num2} = {result:.2f}")
    else:
        print("Invalid choice! ")

        print("=" * 40)
        print("Built with Python | #150DaysOfAI")
        print("=" * 40)

# Run
calculator()